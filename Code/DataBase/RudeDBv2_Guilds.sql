DROP TABLE IF EXISTS `Guilds`;

CREATE TABLE `Guilds` (
  `idGuilds` bigint NOT NULL,
  `penalizeMode` tinyint NOT NULL,
  PRIMARY KEY (`idGuilds`),
  UNIQUE KEY `idGuilds_UNIQUE` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `Guilds` VALUES (794783492197187587,1);
