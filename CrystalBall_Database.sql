-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2024 at 08:44 PM
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
-- Table structure for table `past_predictions`
--

CREATE TABLE `past_predictions` (
  `id` int(11) NOT NULL,
  `home_team` varchar(50) DEFAULT NULL,
  `away_team` varchar(50) DEFAULT NULL,
  `prediction` float DEFAULT NULL,
  `game_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `past_predictions`
--

INSERT INTO `past_predictions` (`id`, `home_team`, `away_team`, `prediction`, `game_date`) VALUES
(1, 'Detroit Tigers', 'Cleveland Guardians', 39.44, '2024-07-30'),
(2, 'Baltimore Orioles', 'Toronto Blue Jays', 55.31, '2024-07-30'),
(3, 'Philadelphia Phillies', 'New York Yankees', 37.62, '2024-07-30'),
(4, 'Tampa Bay Rays', 'Miami Marlins', 70.3, '2024-07-30'),
(5, 'Boston Red Sox', 'Seattle Mariners', 48.56, '2024-07-30'),
(6, 'Cincinnati Reds', 'Chicago Cubs', 56.62, '2024-07-30'),
(7, 'New York Mets', 'Minnesota Twins', 44.47, '2024-07-30'),
(8, 'St. Louis Cardinals', 'Texas Rangers', 54, '2024-07-30'),
(9, 'Chicago White Sox', 'Kansas City Royals', 47.44, '2024-07-30'),
(10, 'Houston Astros', 'Pittsburgh Pirates', 49.32, '2024-07-30'),
(11, 'Milwaukee Brewers', 'Atlanta Braves', 44.08, '2024-07-30'),
(12, 'Los Angeles Angels', 'Colorado Rockies', 75.39, '2024-07-30'),
(13, 'Arizona Diamondbacks', 'Washington Nationals', 56.54, '2024-07-30'),
(14, 'San Diego Padres', 'Los Angeles Dodgers', 38.6, '2024-07-30'),
(15, 'San Francisco Giants', 'Oakland Athletics', 64.37, '2024-07-30');

-- --------------------------------------------------------

--
-- Table structure for table `predictions`
--

CREATE TABLE `predictions` (
  `id` int(11) NOT NULL,
  `home_team` varchar(255) DEFAULT NULL,
  `away_team` varchar(255) DEFAULT NULL,
  `prediction` float DEFAULT NULL,
  `game_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `predictions`
--

INSERT INTO `predictions` (`id`, `home_team`, `away_team`, `prediction`, `game_date`) VALUES
(77, 'Detroit Tigers', 'Cleveland Guardians', 39.44, '2024-07-30'),
(78, 'Baltimore Orioles', 'Toronto Blue Jays', 55.31, '2024-07-30'),
(79, 'Philadelphia Phillies', 'New York Yankees', 37.62, '2024-07-30'),
(80, 'Tampa Bay Rays', 'Miami Marlins', 70.3, '2024-07-30'),
(81, 'Boston Red Sox', 'Seattle Mariners', 48.56, '2024-07-30'),
(82, 'Cincinnati Reds', 'Chicago Cubs', 56.62, '2024-07-30'),
(83, 'New York Mets', 'Minnesota Twins', 44.47, '2024-07-30'),
(84, 'St. Louis Cardinals', 'Texas Rangers', 54, '2024-07-30'),
(85, 'Chicago White Sox', 'Kansas City Royals', 47.44, '2024-07-30'),
(86, 'Houston Astros', 'Pittsburgh Pirates', 49.32, '2024-07-30'),
(87, 'Milwaukee Brewers', 'Atlanta Braves', 44.08, '2024-07-30'),
(88, 'Los Angeles Angels', 'Colorado Rockies', 75.39, '2024-07-30'),
(89, 'Arizona Diamondbacks', 'Washington Nationals', 56.54, '2024-07-30'),
(90, 'San Diego Padres', 'Los Angeles Dodgers', 38.6, '2024-07-30'),
(91, 'San Francisco Giants', 'Oakland Athletics', 64.37, '2024-07-30');

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `teamID` varchar(50) NOT NULL,
  `games_played` int(11) DEFAULT NULL,
  `games_won` int(11) DEFAULT NULL,
  `ERA` decimal(4,2) DEFAULT NULL,
  `OBP` decimal(4,3) DEFAULT NULL,
  `Whip` decimal(4,2) DEFAULT NULL,
  `Slg` decimal(4,3) DEFAULT NULL,
  `win_percentage` decimal(5,4) GENERATED ALWAYS AS (`games_won` / `games_played`) STORED,
  `pythagorean_win_percentage` decimal(5,4) GENERATED ALWAYS AS (pow(`games_won`,2) / (pow(`games_won`,2) + pow(`games_played` - `games_won`,2))) VIRTUAL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`teamID`, `games_played`, `games_won`, `ERA`, `OBP`, `Whip`, `Slg`) VALUES
('Arizona Diamondbacks', 107, 56, 4.53, 0.326, 1.34, 0.416),
('Atlanta Braves', 105, 56, 3.51, 0.302, 1.19, 0.405),
('Baltimore Orioles', 107, 63, 3.81, 0.317, 1.22, 0.452),
('Boston Red Sox', 105, 56, 3.94, 0.327, 1.24, 0.438),
('Chicago Cubs', 108, 51, 3.76, 0.309, 1.24, 0.374),
('Chicago White Sox', 109, 27, 4.70, 0.278, 1.39, 0.344),
('Cincinnati Reds', 106, 51, 3.80, 0.303, 1.24, 0.393),
('Cleveland Guardians', 106, 64, 3.67, 0.311, 1.22, 0.397),
('Colorado Rockies', 107, 38, 5.52, 0.306, 1.53, 0.401),
('Detroit Tigers', 108, 52, 3.96, 0.297, 1.23, 0.386),
('Houston Astros', 106, 55, 4.02, 0.321, 1.30, 0.419),
('Kansas City Royals', 107, 58, 3.82, 0.310, 1.26, 0.410),
('Los Angeles Angels', 106, 46, 4.60, 0.304, 1.32, 0.376),
('Los Angeles Dodgers', 107, 63, 3.79, 0.334, 1.21, 0.436),
('Miami Marlins', 106, 39, 4.48, 0.290, 1.36, 0.362),
('Milwaukee Brewers', 106, 61, 3.73, 0.331, 1.25, 0.402),
('Minnesota Twins', 105, 58, 4.20, 0.324, 1.18, 0.427),
('New York Mets', 106, 56, 4.17, 0.323, 1.30, 0.422),
('New York Yankees', 108, 63, 3.68, 0.334, 1.22, 0.438),
('Oakland Athletics', 108, 44, 4.41, 0.303, 1.35, 0.398),
('Philadelphia Phillies', 106, 65, 3.53, 0.328, 1.17, 0.421),
('Pittsburgh Pirates', 106, 54, 3.81, 0.300, 1.28, 0.369),
('San Diego Padres', 108, 57, 4.06, 0.324, 1.24, 0.411),
('San Francisco Giants', 108, 53, 4.35, 0.316, 1.33, 0.397),
('Seattle Mariners', 108, 56, 3.45, 0.300, 1.08, 0.370),
('St. Louis Cardinals', 106, 54, 4.10, 0.309, 1.28, 0.386),
('Tampa Bay Rays', 106, 54, 4.07, 0.311, 1.24, 0.373),
('Texas Rangers', 107, 52, 4.04, 0.311, 1.26, 0.381),
('Toronto Blue Jays', 107, 50, 4.57, 0.312, 1.32, 0.384),
('Washington Nationals', 107, 49, 4.25, 0.311, 1.31, 0.372);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `past_predictions`
--
ALTER TABLE `past_predictions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_prediction` (`home_team`,`away_team`,`game_date`);

--
-- Indexes for table `predictions`
--
ALTER TABLE `predictions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`teamID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `past_predictions`
--
ALTER TABLE `past_predictions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `predictions`
--
ALTER TABLE `predictions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=92;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
