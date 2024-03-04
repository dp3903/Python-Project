-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 24, 2024 at 06:29 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendify`
--

-- --------------------------------------------------------

--
-- Table structure for table `duhacks2`
--

CREATE TABLE `duhacks2` (
  `username` varchar(20) DEFAULT NULL,
  `attended` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event2`
--

CREATE TABLE `event2` (
  `username` varchar(20) DEFAULT NULL,
  `attended` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event3`
--

CREATE TABLE `event3` (
  `username` varchar(20) DEFAULT NULL,
  `attended` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `event3`
--

INSERT INTO `event3` (`username`, `attended`) VALUES
('u1', 0);

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `ID` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `club` varchar(20) NOT NULL,
  `startDate` datetime NOT NULL,
  `endDate` datetime NOT NULL,
  `image` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`ID`, `name`, `description`, `club`, `startDate`, `endDate`, `image`) VALUES
(4, 'myevent', 'desc', 'c1', '2019-12-13 10:10:10', '2019-12-13 10:10:10', ''),
(5, 'event2', 'desc2', 'c1', '2019-12-13 10:10:10', '2019-12-13 10:10:10', ''),
(6, 'event3', 'desc3', 'c1', '2019-12-13 10:10:10', '2019-12-13 10:10:10', ''),
(9, 'duhacks2', 'Lorem.', 'c1', '2023-02-14 04:40:10', '2023-02-15 04:40:10', '');

-- --------------------------------------------------------

--
-- Table structure for table `myevent`
--

CREATE TABLE `myevent` (
  `username` varchar(20) DEFAULT NULL,
  `attended` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `myevent`
--

INSERT INTO `myevent` (`username`, `attended`) VALUES
('u1', 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`, `email`, `type`) VALUES
('c1', 'abc', '123', 'club'),
('u1', 'abc', '123', 'student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `duhacks2`
--
ALTER TABLE `duhacks2`
  ADD KEY `username` (`username`);

--
-- Indexes for table `event2`
--
ALTER TABLE `event2`
  ADD KEY `username` (`username`);

--
-- Indexes for table `event3`
--
ALTER TABLE `event3`
  ADD KEY `username` (`username`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `club` (`club`);

--
-- Indexes for table `myevent`
--
ALTER TABLE `myevent`
  ADD KEY `username` (`username`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `duhacks2`
--
ALTER TABLE `duhacks2`
  ADD CONSTRAINT `duhacks2_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`);

--
-- Constraints for table `event2`
--
ALTER TABLE `event2`
  ADD CONSTRAINT `event2_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`);

--
-- Constraints for table `event3`
--
ALTER TABLE `event3`
  ADD CONSTRAINT `event3_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`);

--
-- Constraints for table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `events_ibfk_1` FOREIGN KEY (`club`) REFERENCES `users` (`username`);

--
-- Constraints for table `myevent`
--
ALTER TABLE `myevent`
  ADD CONSTRAINT `myevent_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
