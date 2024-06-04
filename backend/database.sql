CREATE DATABASE baseball_stats;
USE baseball_stats;

CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    game_date DATE,
    game_number CHAR(1),
    day_of_week VARCHAR(3),
    visiting_team VARCHAR(3),
    visiting_team_league VARCHAR(2),
    visiting_team_game_number INT,
    home_team VARCHAR(3),
    home_team_league VARCHAR(2),
    home_team_game_number INT,
    visiting_team_score INT,
    home_team_score INT,
    park_id VARCHAR(5),
    visiting_line_score VARCHAR(20),
    home_line_score VARCHAR(20)
);

CREATE TABLE team_offensive_stats (
    stats_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    team_type ENUM('visiting', 'home'),
    at_bats INT,
    hits INT,
    doubles INT,
    triples INT,
    homeruns INT,
    rbi INT,
    sacrifice_hits INT,
    sacrifice_flies INT,
    hit_by_pitch INT,
    walks INT,
    intentional_walks INT,
    strikeouts INT,
    stolen_bases INT,
    caught_stealing INT,
    grounded_into_double_plays INT,
    awarded_first_on_catcher_interference INT,
    left_on_base INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);


CREATE TABLE team_pitching_stats (
    stats_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    team_type ENUM('visiting', 'home'),
    pitchers_used INT,
    individual_earned_runs INT,
    team_earned_runs INT,
    wild_pitches INT,
    balks INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);

CREATE TABLE team_defensive_stats (
    stats_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    team_type ENUM('visiting', 'home'),
    putouts INT,
    assists INT,
    errors INT,
    passed_balls INT,
    double_plays INT,
    triple_plays INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);





