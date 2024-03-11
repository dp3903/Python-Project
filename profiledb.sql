-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 11, 2024 at 02:09 PM
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
-- Database: `profiledb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_users'),
(22, 'Can change user', 6, 'change_users'),
(23, 'Can delete user', 6, 'delete_users'),
(24, 'Can view user', 6, 'view_users'),
(25, 'Can add template', 7, 'add_template'),
(26, 'Can change template', 7, 'change_template'),
(27, 'Can delete template', 7, 'delete_template'),
(28, 'Can view template', 7, 'view_template'),
(29, 'Can add app logs', 8, 'add_applogs'),
(30, 'Can change app logs', 8, 'change_applogs'),
(31, 'Can delete app logs', 8, 'delete_applogs'),
(32, 'Can view app logs', 8, 'view_applogs');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'profileApp', 'users'),
(5, 'sessions', 'session'),
(8, 'templateData', 'applogs'),
(7, 'templateData', 'template');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-03-09 18:13:34.480847'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-03-09 18:13:34.517615'),
(3, 'auth', '0001_initial', '2024-03-09 18:13:34.665604'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-03-09 18:13:34.715085'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-03-09 18:13:34.715085'),
(6, 'auth', '0004_alter_user_username_opts', '2024-03-09 18:13:34.732201'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-03-09 18:13:34.752528'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-03-09 18:13:34.752528'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-03-09 18:13:34.764980'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-03-09 18:13:34.770342'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-03-09 18:13:34.770342'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-03-09 18:13:34.787624'),
(13, 'auth', '0011_update_proxy_permissions', '2024-03-09 18:13:34.795952'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-03-09 18:13:34.802582'),
(15, 'profileApp', '0001_initial', '2024-03-09 18:13:34.982499'),
(16, 'admin', '0001_initial', '2024-03-09 18:13:35.068824'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-03-09 18:13:35.074856'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-09 18:13:35.080237'),
(19, 'sessions', '0001_initial', '2024-03-09 18:13:35.103320'),
(20, 'templateData', '0001_initial', '2024-03-09 18:13:35.248140');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('qyvklnfq22ncxt4zcg5btc56co8sy4x1', '.eJxVjEEOwiAQRe_C2hAKI7Qu3XsGMswMUjU0Ke3KeHdD0oVu_3vvv1XEfStxb7LGmdVFDer0uyWkp9QO-IH1vmha6rbOSXdFH7Tp28Lyuh7u30HBVnptM1KCfA4uWAriHRrJAJjRGUucZRwdeYbBEEoWdjzBFCCIMz5Zrz5fEO44wA:1rj2NB:8wzhNFnb3OLISzT-26dN0S_qXoXvI8cWD7bFyPE2aic', '2024-03-23 19:28:45.980975');

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
(1, 'pbkdf2_sha256$600000$GRwYlNLtzSIyZXjr4l3nMF$ngVdDboXS6BfCPrlNeaUlr4eriicaaAWuUmD7X8wcjY=', '2024-03-09 19:28:45.978059', 0, 'Nisarg', '', '', 'patel123@gmail.com', 0, 1, '2024-03-09 18:14:31.702668', 'static/img1.jpg'),
(2, 'pbkdf2_sha256$600000$oh8I1rOJfqUMChvbxph9PQ$qfIVhugV5Gdz16/qmRSYrlaP1E5d6pifuT71S0AC7Ns=', '2024-03-09 19:18:58.053868', 0, 'Jainish', '', '', 'patel456@gmail.com', 0, 1, '2024-03-09 19:15:14.528987', 'static/img1_vB3vZsk.jpg'),
(3, 'pbkdf2_sha256$600000$4mwDubvB2AZpfMWVReA1jJ$X3ApeINq1IfCC8fc2e8jLAG5DWpZ6ASPnqxKqd+HQew=', '2024-03-11 12:49:39.540974', 0, 'dhruv', '', '', 'abc@gmail.com', 0, 1, '2024-03-11 12:49:38.938589', 'static/wallpaperflare.com_wallpaper_1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `profileapp_users_groups`
--

CREATE TABLE `profileapp_users_groups` (
  `id` bigint(20) NOT NULL,
  `users_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profileapp_users_user_permissions`
--

CREATE TABLE `profileapp_users_user_permissions` (
  `id` bigint(20) NOT NULL,
  `users_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `templatedata_applogs`
--

CREATE TABLE `templatedata_applogs` (
  `id` bigint(20) NOT NULL,
  `transaction_type` varchar(10) NOT NULL,
  `TID_id` varchar(10) NOT NULL,
  `UID_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `templatedata_template`
--

CREATE TABLE `templatedata_template` (
  `templateId` varchar(10) NOT NULL,
  `templateName` varchar(20) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  `templateZip` varchar(100) NOT NULL,
  `totaldownloads` int(11) NOT NULL,
  `UID_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `templatedata_template`
--

INSERT INTO `templatedata_template` (`templateId`, `templateName`, `description`, `date`, `templateZip`, `totaldownloads`, `UID_id`) VALUES
('2_card', 'card', 'this is html card.', '2024-03-09', 'static/templates/tempFiles/2_card', 0, 2),
('2_my temp', 'my temp', 'some random desc', '2024-03-09', 'static/templates/tempFiles/2_my temp', 0, 2),
('2_signUp', 'signUp', 'this is signUp template.', '2024-03-09', 'static/templates/tempFiles/2_signUp', 0, 2),
('2_temp1', 'temp1', 'some random desc', '2024-03-09', 'static/templates/tempFiles/2_temp1', 0, 2),
('2_temp2', 'temp2', 'some random desc', '2024-03-09', 'static/templates/tempFiles/2_temp2', 0, 2),
('2_temp3', 'temp3', 'some random desc', '2024-03-09', 'static/templates/tempFiles/2_temp3', 0, 2),
('3_temp1', 'temp1', 'some random desc', '2024-03-09', 'static/templates/tempFiles/3_temp1', 0, 3),
('3_temp2', 'temp2', 'some random desc', '2024-03-09', 'static/templates/tempFiles/3_temp2', 0, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_profileApp_users_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `profileapp_users`
--
ALTER TABLE `profileapp_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `profileapp_users_groups`
--
ALTER TABLE `profileapp_users_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profileApp_users_groups_users_id_group_id_79ccb948_uniq` (`users_id`,`group_id`),
  ADD KEY `profileApp_users_groups_group_id_f7967294_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `profileapp_users_user_permissions`
--
ALTER TABLE `profileapp_users_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profileApp_users_user_pe_users_id_permission_id_eace3454_uniq` (`users_id`,`permission_id`),
  ADD KEY `profileApp_users_use_permission_id_9753e457_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `templatedata_applogs`
--
ALTER TABLE `templatedata_applogs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `templateData_applogs_TID_id_1bead615_fk_templateD` (`TID_id`),
  ADD KEY `templateData_applogs_UID_id_086a186f_fk_profileApp_users_id` (`UID_id`);

--
-- Indexes for table `templatedata_template`
--
ALTER TABLE `templatedata_template`
  ADD PRIMARY KEY (`templateId`),
  ADD KEY `templateData_template_UID_id_66829ccd_fk_profileApp_users_id` (`UID_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `profileapp_users`
--
ALTER TABLE `profileapp_users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `profileapp_users_groups`
--
ALTER TABLE `profileapp_users_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profileapp_users_user_permissions`
--
ALTER TABLE `profileapp_users_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `templatedata_applogs`
--
ALTER TABLE `templatedata_applogs`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_profileApp_users_id` FOREIGN KEY (`user_id`) REFERENCES `profileapp_users` (`id`);

--
-- Constraints for table `profileapp_users_groups`
--
ALTER TABLE `profileapp_users_groups`
  ADD CONSTRAINT `profileApp_users_groups_group_id_f7967294_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `profileApp_users_groups_users_id_aecdd4dc_fk_profileApp_users_id` FOREIGN KEY (`users_id`) REFERENCES `profileapp_users` (`id`);

--
-- Constraints for table `profileapp_users_user_permissions`
--
ALTER TABLE `profileapp_users_user_permissions`
  ADD CONSTRAINT `profileApp_users_use_permission_id_9753e457_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `profileApp_users_use_users_id_72b1e0ef_fk_profileAp` FOREIGN KEY (`users_id`) REFERENCES `profileapp_users` (`id`);

--
-- Constraints for table `templatedata_applogs`
--
ALTER TABLE `templatedata_applogs`
  ADD CONSTRAINT `templateData_applogs_TID_id_1bead615_fk_templateD` FOREIGN KEY (`TID_id`) REFERENCES `templatedata_template` (`templateId`),
  ADD CONSTRAINT `templateData_applogs_UID_id_086a186f_fk_profileApp_users_id` FOREIGN KEY (`UID_id`) REFERENCES `profileapp_users` (`id`);

--
-- Constraints for table `templatedata_template`
--
ALTER TABLE `templatedata_template`
  ADD CONSTRAINT `templateData_template_UID_id_66829ccd_fk_profileApp_users_id` FOREIGN KEY (`UID_id`) REFERENCES `profileapp_users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
