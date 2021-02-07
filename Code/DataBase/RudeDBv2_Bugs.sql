DROP TABLE IF EXISTS `Bugs`;

CREATE TABLE `Bugs` (
  `idBugs` int NOT NULL AUTO_INCREMENT,
  `Comment` text COLLATE utf8_bin NOT NULL,
  `idGuildBugs` bigint NOT NULL,
  PRIMARY KEY (`idBugs`),
  UNIQUE KEY `idBugs_UNIQUE` (`idBugs`),
  KEY `fk_Bugs_1_idx` (`idGuildBugs`),
  CONSTRAINT `fk_Bugs_1` FOREIGN KEY (`idGuildBugs`) REFERENCES `Guilds` (`idGuilds`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `Bugs` VALUES (1,'Los requests no se mandan :(',794783492197187587);
