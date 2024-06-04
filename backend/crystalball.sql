-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2024 at 11:16 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crystalball`
--

-- --------------------------------------------------------

--
-- Table structure for table `games`
--

CREATE TABLE `games` (
  `game_id` int(11) NOT NULL,
  `game_date` date DEFAULT NULL,
  `game_number` char(1) DEFAULT NULL,
  `day_of_week` varchar(3) DEFAULT NULL,
  `visiting_team` varchar(3) DEFAULT NULL,
  `visiting_team_league` varchar(2) DEFAULT NULL,
  `visiting_team_game_number` int(11) DEFAULT NULL,
  `home_team` varchar(3) DEFAULT NULL,
  `home_team_league` varchar(2) DEFAULT NULL,
  `home_team_game_number` int(11) DEFAULT NULL,
  `visiting_team_score` int(11) DEFAULT NULL,
  `home_team_score` int(11) DEFAULT NULL,
  `park_id` varchar(5) DEFAULT NULL,
  `visiting_line_score` varchar(20) DEFAULT NULL,
  `home_line_score` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `team_defensive_stats`
--

CREATE TABLE `team_defensive_stats` (
  `stats_id` int(11) NOT NULL,
  `game_id` int(11) DEFAULT NULL,
  `team_type` enum('visiting','home') DEFAULT NULL,
  `putouts` int(11) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `errors` int(11) DEFAULT NULL,
  `passed_balls` int(11) DEFAULT NULL,
  `double_plays` int(11) DEFAULT NULL,
  `triple_plays` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `team_offensive_stats`
--

CREATE TABLE `team_offensive_stats` (
  `stats_id` int(11) NOT NULL,
  `game_id` int(11) DEFAULT NULL,
  `team_type` enum('visiting','home') DEFAULT NULL,
  `at_bats` int(11) DEFAULT NULL,
  `hits` int(11) DEFAULT NULL,
  `doubles` int(11) DEFAULT NULL,
  `triples` int(11) DEFAULT NULL,
  `homeruns` int(11) DEFAULT NULL,
  `rbi` int(11) DEFAULT NULL,
  `sacrifice_hits` int(11) DEFAULT NULL,
  `sacrifice_flies` int(11) DEFAULT NULL,
  `hit_by_pitch` int(11) DEFAULT NULL,
  `walks` int(11) DEFAULT NULL,
  `intentional_walks` int(11) DEFAULT NULL,
  `strikeouts` int(11) DEFAULT NULL,
  `stolen_bases` int(11) DEFAULT NULL,
  `caught_stealing` int(11) DEFAULT NULL,
  `grounded_into_double_plays` int(11) DEFAULT NULL,
  `awarded_first_on_catcher_interference` int(11) DEFAULT NULL,
  `left_on_base` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `team_pitching_stats`
--

CREATE TABLE `team_pitching_stats` (
  `stats_id` int(11) NOT NULL,
  `game_id` int(11) DEFAULT NULL,
  `team_type` enum('visiting','home') DEFAULT NULL,
  `pitchers_used` int(11) DEFAULT NULL,
  `individual_earned_runs` int(11) DEFAULT NULL,
  `team_earned_runs` int(11) DEFAULT NULL,
  `wild_pitches` int(11) DEFAULT NULL,
  `balks` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `games`
--
ALTER TABLE `games`
  ADD PRIMARY KEY (`game_id`);

--
-- Indexes for table `team_defensive_stats`
--
ALTER TABLE `team_defensive_stats`
  ADD PRIMARY KEY (`stats_id`),
  ADD KEY `game_id` (`game_id`);

--
-- Indexes for table `team_offensive_stats`
--
ALTER TABLE `team_offensive_stats`
  ADD PRIMARY KEY (`stats_id`),
  ADD KEY `game_id` (`game_id`);

--
-- Indexes for table `team_pitching_stats`
--
ALTER TABLE `team_pitching_stats`
  ADD PRIMARY KEY (`stats_id`),
  ADD KEY `game_id` (`game_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `games`
--
ALTER TABLE `games`
  MODIFY `game_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `team_defensive_stats`
--
ALTER TABLE `team_defensive_stats`
  MODIFY `stats_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `team_offensive_stats`
--
ALTER TABLE `team_offensive_stats`
  MODIFY `stats_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `team_pitching_stats`
--
ALTER TABLE `team_pitching_stats`
  MODIFY `stats_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `team_defensive_stats`
--
ALTER TABLE `team_defensive_stats`
  ADD CONSTRAINT `team_defensive_stats_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`);

--
-- Constraints for table `team_offensive_stats`
--
ALTER TABLE `team_offensive_stats`
  ADD CONSTRAINT `team_offensive_stats_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`);

--
-- Constraints for table `team_pitching_stats`
--
ALTER TABLE `team_pitching_stats`
  ADD CONSTRAINT `team_pitching_stats_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
