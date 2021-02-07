DROP TABLE IF EXISTS `Stories`;

CREATE TABLE `Stories` (
  `idStories` int NOT NULL AUTO_INCREMENT,
  `userId` bigint NOT NULL,
  `warnings` int NOT NULL,
  `guildIdSty` bigint NOT NULL,
  PRIMARY KEY (`idStories`),
  UNIQUE KEY `idStories_UNIQUE` (`idStories`),
  KEY `fk_Stories_1_idx` (`guildIdSty`),
  CONSTRAINT `fk_Stories_1` FOREIGN KEY (`guildIdSty`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
