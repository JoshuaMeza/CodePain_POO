DROP TABLE IF EXISTS `Whitelist`;

CREATE TABLE `Whitelist` (
  `idWhitelist` int NOT NULL AUTO_INCREMENT,
  `idUser` bigint NOT NULL,
  `idGuild` bigint NOT NULL,
  PRIMARY KEY (`idWhitelist`),
  UNIQUE KEY `idWhitelist_UNIQUE` (`idWhitelist`),
  KEY `fk_Whitelist_1_idx` (`idGuild`),
  CONSTRAINT `fk_Whitelist_1` FOREIGN KEY (`idGuild`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `Whitelist` VALUES (1,572589109412102228,794783492197187587);
