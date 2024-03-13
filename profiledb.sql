-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 13, 2024 at 12:57 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `profiledb`
--

-- --------------------------------------------------------

--
-- Table structure for table `profileapp_users`
--

CREATE TABLE `profileapp_users` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `profile_img` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profileapp_users`
--

INSERT INTO `profileapp_users` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `profile_img`) VALUES
(2, 'pbkdf2_sha256$600000$oh8I1rOJfqUMChvbxph9PQ$qfIVhugV5Gdz16/qmRSYrlaP1E5d6pifuT71S0AC7Ns=', '2024-03-09 19:18:58.053868', 0, 'Jainish', '', '', 'patel456@gmail.com', 0, 1, '2024-03-09 19:15:14.528987', 'static/img1_vB3vZsk.jpg'),
(3, 'pbkdf2_sha256$600000$4mwDubvB2AZpfMWVReA1jJ$X3ApeINq1IfCC8fc2e8jLAG5DWpZ6ASPnqxKqd+HQew=', '2024-03-13 10:15:08.157323', 0, 'dhruv', '', '', 'abd@gmail.com', 0, 1, '2024-03-11 12:49:38.938589', 'static/wallpaperflare.com_wallpaper_1.jpg'),
(4, 'pbkdf2_sha256$600000$Q3ADbWRi49VxwHjxhPabmk$qy/J1NATwZ9q4T8E3w1atjesQLi8PeDsdU6bLn8JvA4=', '2024-03-13 11:52:44.464739', 0, 'Nisarg', '', '', 'patel123@gmail.com', 0, 1, '2024-03-13 11:52:44.052425', 'static/img1.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `profileapp_users`
--
ALTER TABLE `profileapp_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `profileapp_users`
--
ALTER TABLE `profileapp_users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
