#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <fstream>
#include <sstream>
#include <bitset>

//uso
//Comprimir
//./huffman -c entrada.txt salida.huff
//Descomprimir
//./huffman -d salida.huff recuperado.txt


struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f, Node* l = nullptr, Node* r = nullptr) {
        ch = c;
        freq = f;
        left = l;
        right = r;
    }
};


struct CompareNode {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

void deleteTree(Node* root) {
    if (root == nullptr) {
        return;
    }
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}


void generateCodes(Node* root, std::string str, std::map<char, std::string>& huffmanCode) {
    if (root == nullptr) {
        return;
    }

    if (!root->left && !root->right) {
        huffmanCode[root->ch] = str;
    }
    
    generateCodes(root->left, str + "0", huffmanCode);
    generateCodes(root->right, str + "1", huffmanCode);
}

Node* buildHuffmanTree(const std::map<char, int>& freqMap) {
    std::priority_queue<Node*, std::vector<Node*>, CompareNode> pq;

    for (auto const& pair : freqMap) {
        pq.push(new Node(pair.first, pair.second));
    }
    
    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();
        Node* right = pq.top();
        pq.pop();

        int sumFreq = left->freq + right->freq;
        Node* parent = new Node('$', sumFreq, left, right);

        pq.push(parent);
    }
    
    return pq.top();
}

std::string encodeData(const std::string& data, const std::map<char, std::string>& huffmanCode) {
    std::string encodedData = "";
    for (char ch : data) {
        encodedData += huffmanCode.at(ch);
    }
    return encodedData;
}

std::string decodeData(const std::string& encodedData, Node* root) {
    if (root == nullptr) {
        return "";
    }
    std::string decodedData = "";
    Node* current = root;

    for (char bit : encodedData) {
        if (bit == '0') {
            current = current->left;
        } else {
            current = current->right;
        }

        if (!current->left && !current->right) {
            decodedData += current->ch;
            current = root;
        }
    }
    return decodedData;
}

void writeBinaryFile(const std::string& filename, const std::map<char, std::string>& huffmanCode, const std::string& encodedData) {
    std::ofstream file(filename, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Error: No se pudo abrir el archivo para escritura." << std::endl;
        return;
    }
    
    for (const auto& pair : huffmanCode) {
        file << pair.first << ":" << pair.second << "\n";
    }
    file << "EOF\n";

    int padding = (8 - (encodedData.length() % 8)) % 8;
    file.put(static_cast<unsigned char>(padding));
    
    for (size_t i = 0; i < encodedData.length(); i += 8) {
        std::string byteStr = encodedData.substr(i, 8);
        if (byteStr.length() < 8) {
            byteStr.append(8 - byteStr.length(), '0');
        }
        unsigned char byte = static_cast<unsigned char>(std::bitset<8>(byteStr).to_ulong());
        file.put(byte);
    }
    
    file.close();
}

void readBinaryFile(const std::string& filename, std::string& decodedData, std::map<char, std::string>& huffmanCode) {
    std::ifstream file(filename, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Error: No se pudo abrir el archivo para lectura." << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line) && line != "EOF") {
        size_t colonPos = line.find(':');
        if (colonPos != std::string::npos) {
            char key = line[0];
            std::string value = line.substr(colonPos + 1);
            huffmanCode[key] = value;
        }
    }
    
    if (file.eof()) {
        std::cerr << "Error: No se encontró el marcador de fin de encabezado (EOF)." << std::endl;
        return;
    }
    
    unsigned char paddingByte;
    file.read(reinterpret_cast<char*>(&paddingByte), 1);
    int padding = static_cast<int>(paddingByte);

    std::string encodedString = "";
    unsigned char byte;
    while (file.read(reinterpret_cast<char*>(&byte), 1)) {
        encodedString += std::bitset<8>(byte).to_string();
    }
    
    file.close();

    if (padding > 0) {
        encodedString.resize(encodedString.length() - padding);
    }
    
    Node* root = new Node('$', 0);
    for (const auto& pair : huffmanCode) {
        Node* current = root;
        for (char bit : pair.second) {
            if (bit == '0') {
                if (!current->left) {
                    current->left = new Node('$', 0);
                }
                current = current->left;
            } else {
                if (!current->right) {
                    current->right = new Node('$', 0);
                }
                current = current->right;
            }
        }
        current->ch = pair.first;
    }
    
    decodedData = decodeData(encodedString, root);
    deleteTree(root);
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cerr << "Uso: " << argv[0] << " <-c|-d> <archivo_entrada> <archivo_salida>" << std::endl;
        return 1;
    }
    
    std::string mode = argv[1];
    std::string inputFile = argv[2];
    std::string outputFile = argv[3];
    
    if (mode == "-c") {
        // Modo compresion
        std::ifstream inFile(inputFile);
        if (!inFile.is_open()) {
            std::cerr << "Error: No se pudo abrir el archivo de entrada." << std::endl;
            return 1;
        }
        std::string data((std::istreambuf_iterator<char>(inFile)), std::istreambuf_iterator<char>());
        inFile.close();
        
        // Contar frecuencias
        std::map<char, int> freqMap;
        for (char ch : data) {
            freqMap[ch]++;
        }
        
        Node* root = buildHuffmanTree(freqMap);
        std::map<char, std::string> huffmanCode;
        generateCodes(root, "", huffmanCode);
        
        std::string encodedData = encodeData(data, huffmanCode);
        writeBinaryFile(outputFile, huffmanCode, encodedData);
        
        std::cout << "Compresion exitosa. Archivo guardado como " << outputFile << std::endl;
        
        deleteTree(root);
        
    } else if (mode == "-d") {
        std::string decodedData;
        std::map<char, std::string> huffmanCode;
        readBinaryFile(inputFile, decodedData, huffmanCode);

        if (!decodedData.empty()) {
            std::ofstream outFile(outputFile);
            if (!outFile.is_open()) {
                std::cerr << "Error: No se pudo abrir el archivo de salida." << std::endl;
                return 1;
            }
            outFile << decodedData;
            outFile.close();
            std::cout << "Descompresion exitosa. Archivo guardado como " << outputFile << std::endl;
        } else {
            std::cerr << "Error: La decodificación falló. El archivo de salida puede estar vacío." << std::endl;
            return 1;
        }
        
    } else {
        std::cerr << "Modo invalido. Usa -c para comprimir o -d para descomprimir." << std::endl;
        return 1;
    }
    
    return 0;
}
