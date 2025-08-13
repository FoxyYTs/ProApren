CREATE TABLE `paciente` (
  `id_paciente` int(11) NOT NULL,
  `nombre_paciente` varchar(255) NOT NULL,
  `apellido_paciente` varchar(255) NOT NULL,
  `fecha_paciente` date NOT NULL,
  `genero_paciente` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `paciente` (`id_paciente`, `nombre_paciente`, `apellido_paciente`, `fecha_paciente`, `genero_paciente`) VALUES
(1, 'Pedro', 'Pascal', '2020-03-15', 'Masculino'),
(2, 'Gran', 'Anatoli', '2020-03-15', 'Masculino'),
(3, 'Gran', 'Torino', '2020-03-15', 'Masculino'),
(4, 'Carmen', 'Electra', '2020-03-15', 'Femenino');

CREATE TABLE `medico` (
  `id_medico` int(11) NOT NULL,
  `nombre_medico` varchar(255) NOT NULL,
  `apellido_medico` varchar(255) NOT NULL,
  `id_especialidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `medico` (`id_medico`, `nombre_medico`, `apellido_medico`, `id_especialidad`) VALUES
(1, 'Paquita', 'Barrio', 1),
(2, 'Jose', 'Maria', 2),
(3, 'Doctor', 'Mario', 3),
(4, 'Morgan', 'HombreLibre', 4);

CREATE TABLE `especialidad` (
  `id_especialidad` int(11) NOT NULL,
  `nombre_especialidad` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `especialidad` (`id_especialidad`, `nombre_especialidad`) VALUES
(1, 'Medico General'),
(2, 'Pediatra'),
(3, 'Cardiologo'),
(4, 'Otorrinolaringologo');

CREATE TABLE `cita_medica` (
  `id_cita` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `id_medico` int(11) NOT NULL,
  `diagnostico_cita` text NOT NULL,
  `fecha_cita` dateTime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `cita_medica` (`id_cita`, `id_paciente`, `id_medico`, `diagnostico_cita`, `fecha_cita`) VALUES 
(1, '1', '4', 'Gripe', '2025-06-09 19:16:37'),
(2, '2', '3', 'Faringitis', '2025-05-09 19:16:37'),
(3, '3', '2', 'Alergia', '2025-02-09 19:16:37'),
(4, '4', '1', 'Arritmia', '2025-08-09 19:16:37');

ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id_paciente`);

ALTER TABLE `medico`
  ADD PRIMARY KEY (`id_medico`),
  ADD KEY `id_especialidad` (`id_especialidad`);

ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`id_especialidad`);

ALTER TABLE `cita_medica`
  ADD PRIMARY KEY (`id_cita`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `id_medico` (`id_medico`);

ALTER TABLE `paciente`
  MODIFY `id_paciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `medico`
  MODIFY `id_medico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `especialidad`
  MODIFY `id_especialidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `cita_medica`
  MODIFY `id_cita` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `medico`
  ADD CONSTRAINT `medico_ibfk_1` FOREIGN KEY (`id_especialidad`) REFERENCES `especialidad` (`id_especialidad`);

ALTER TABLE `cita_medica`
  ADD CONSTRAINT `cita_medica_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id_paciente`),
  ADD CONSTRAINT `cita_medica_ibfk_2` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id_medico`);

