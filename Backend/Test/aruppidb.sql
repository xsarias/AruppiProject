-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-04-2024 a las 09:05:14
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `aruppidb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anime`
--

CREATE TABLE `anime` (
  `id` int(11) NOT NULL,
  `contentName` varchar(50) NOT NULL,
  `url` varchar(100) NOT NULL,
  `image` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `type` varchar(30) NOT NULL,
  `episodeAmount` int(11) NOT NULL,
  `category` varchar(30) NOT NULL,
  `animationEstudio` varchar(40) NOT NULL,
  `producer` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `anime`
--

INSERT INTO `anime` (`id`, `contentName`, `url`, `image`, `description`, `type`, `episodeAmount`, `category`, `animationEstudio`, `producer`) VALUES
(1, 'Naruto', 'https://www.ejemplo.com/naruto', 'naruto.jpg', 'Naruto es una serie de anime...', 'Serie', 220, 'Action', 'Studio Pierrot', 'Producer1'),
(2, 'One Piece', 'https://www.ejemplo.com/one-piece', 'one_piece.jpg', 'One Piece sigue las aventuras de Monkey D. Luffy...', 'Serie', 1000, 'Adventure', 'Toei Animation', 'Producer2'),
(3, 'Dragon Ball Z', 'https://www.ejemplo.com/dragon-ball-z', 'dragon_ball_z.jpg', 'Dragon Ball Z sigue las aventuras de Goku...', 'Serie', 291, 'Action', 'Toei Animation', 'Producer1'),
(4, 'Attack on Titan', 'https://www.ejemplo.com/attack-on-titan', 'attack_on_titan.jpg', 'Attack on Titan se desarrolla en un mundo...', 'Serie', 75, 'Action', 'Wit Studio', 'Producer3'),
(5, 'My Hero Academia', 'https://www.ejemplo.com/my-hero-academia', 'my_hero_academia.jpg', 'My Hero Academia se desarrolla en un mundo...', 'Serie', 113, 'Action', 'Studio Bones', 'Producer3'),
(6, 'Death Note', 'https://www.ejemplo.com/death-note', 'death_note.jpg', 'Death Note sigue la historia de Light Yagami...', 'Serie', 37, 'Mystery', 'Madhouse', 'Producer4'),
(7, 'Fullmetal Alchemist: Brotherhood', 'https://www.ejemplo.com/fullmetal-alchemist-brotherhood', 'fullmetal_alchemist_brotherhood.jpg', 'Fullmetal Alchemist: Brotherhood sigue las aventuras...', 'Serie', 64, 'Action', 'Bones', 'Producer4'),
(8, 'Demon Slayer: Kimetsu no Yaiba', 'https://www.ejemplo.com/demon-slayer-kimetsu-no-yaiba', 'demon_slayer_kimetsu_no_yaiba.jpg', 'Demon Slayer: Kimetsu no Yaiba sigue la historia de Tanjiro Kamado...', 'Serie', 26, 'Action', 'ufotable', 'Producer5'),
(9, 'One Punch Man', 'https://www.ejemplo.com/one-punch-man', 'one_punch_man.jpg', 'One Punch Man sigue la historia de Saitama...', 'Serie', 24, 'Action', 'Madhouse', 'Producer5'),
(10, 'Sword Art Online', 'https://www.ejemplo.com/sword-art-online', 'sword_art_online.jpg', 'Sword Art Online se desarrolla en un futuro...', 'Serie', 97, 'Adventure', 'A-1 Pictures', 'Producer6');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favorites`
--

CREATE TABLE `favorites` (
  `UserId` int(10) NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `favorites`
--

INSERT INTO `favorites` (`UserId`, `id`) VALUES
(81177, 7),
(123811, 1),
(123811, 5),
(495407, 7),
(876316, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `manga`
--

CREATE TABLE `manga` (
  `id` int(11) NOT NULL,
  `ContentName` varchar(50) NOT NULL,
  `url` varchar(100) NOT NULL,
  `Image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `manga`
--

INSERT INTO `manga` (`id`, `ContentName`, `url`, `Image`) VALUES
(21, 'Attack on Titan', 'https://www.ejemplo.com/attack-on-titan', 'attack_on_titan.jpg'),
(22, 'My Hero Academia', 'https://www.ejemplo.com/my-hero-academia', 'my_hero_academia.jpg'),
(23, 'Naruto', 'https://www.ejemplo.com/naruto', 'naruto.jpg'),
(24, 'One Piece', 'https://www.ejemplo.com/one-piece', 'one_piece.jpg'),
(25, 'Tokyo Ghoul', 'https://www.ejemplo.com/tokyo-ghoul', 'tokyo_ghoul.jpg'),
(26, 'Bleach', 'https://www.ejemplo.com/bleach', 'bleach.jpg'),
(27, 'Fullmetal Alchemist', 'https://www.ejemplo.com/fullmetal-alchemist', 'fullmetal_alchemist.jpg'),
(28, 'Death Note', 'https://www.ejemplo.com/death-note', 'death_note.jpg'),
(29, 'Demon Slayer: Kimetsu no Yaiba', 'https://www.ejemplo.com/demon-slayer-kimetsu-no-yaiba', 'demon_slayer.jpg'),
(30, 'One Punch Man', 'https://www.ejemplo.com/one-punch-man', 'one_punch_man.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `contentName` varchar(30) NOT NULL,
  `url` varchar(100) NOT NULL,
  `image` varchar(50) NOT NULL,
  `information` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `news`
--

INSERT INTO `news` (`id`, `contentName`, `url`, `image`, `information`) VALUES
(31, 'Sakura en flor', 'url1', 'imagen1.jpg', 'El florecimiento de los cerezos en Japón es uno de los eventos más esperados del año, atrayendo a turistas de todo el mundo.'),
(32, 'Templos antiguos', 'url2', 'imagen2.jpg', 'Descubre la historia y la belleza de los antiguos templos de Kioto, testigos del rico patrimonio cultural de Japón.'),
(33, 'Cultura del té', 'url3', 'imagen3.jpg', 'Sumérgete en la tranquila ceremonia del té japonés y aprende sobre la espiritualidad y la elegancia de esta tradición centenaria.'),
(34, 'Samuráis legendarios', 'url4', 'imagen4.jpg', 'Explora la fascinante historia de los samuráis japoneses, guerreros valientes y honorables que dominaron el antiguo Japón.'),
(35, 'Gastronomía japonesa', 'url5', 'imagen5.jpg', 'Embárcate en un viaje culinario por Japón y descubre los sabores únicos de sushi, ramen, tempura y mucho más.'),
(36, 'Arte del origami', 'url6', 'imagen6.jpg', 'Aprende el arte del origami, la antigua técnica japonesa de plegado de papel, que simboliza la creatividad y la paciencia.'),
(37, 'Festivales tradicionales', 'url7', 'imagen7.jpg', 'Únete a las festividades japonesas y experimenta la alegría y el colorido de los festivales tradicionales, como el Matsuri y el Hanami.'),
(38, 'Jardines zen', 'url8', 'imagen8.jpg', 'Relájate en los serenos jardines zen de Japón, diseñados para inspirar calma, meditación y contemplación.'),
(39, 'Arte del manga', 'url9', 'imagen9.jpg', 'Sumérgete en el emocionante mundo del manga japonés y descubre las historias vívidas y los personajes icónicos de este género único.'),
(40, 'Geishas elegantes', 'url10', 'imagen10.jpg', 'Explora el mundo misterioso y sofisticado de las geishas japonesas, símbolos de gracia, belleza y tradición en la cultura japonesa.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `progress`
--

CREATE TABLE `progress` (
  `UserId` int(10) NOT NULL,
  `id` int(10) NOT NULL,
  `NumberEpisodes` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `progress`
--

INSERT INTO `progress` (`UserId`, `id`, `NumberEpisodes`) VALUES
(81177, 5, 34),
(262664, 9, 234),
(495407, 3, 3),
(532861, 7, 23),
(782996, 2, 1),
(782996, 8, 23),
(495407, 3, 4),
(495407, 3, 5),
(495407, 6, 1),
(495407, 6, 4),
(495407, 4, 20),
(495407, 6, 1),
(495407, 6, 4),
(495407, 4, 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `queue`
--

CREATE TABLE `queue` (
  `UserId` int(10) NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `queue`
--

INSERT INTO `queue` (`UserId`, `id`) VALUES
(81177, 5),
(123811, 2),
(262664, 2),
(262664, 3),
(262664, 5),
(262664, 6),
(495407, 3),
(782996, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `radio`
--

CREATE TABLE `radio` (
  `id` int(10) NOT NULL,
  `ContenName` varchar(50) NOT NULL,
  `url` varchar(100) NOT NULL,
  `Image` varchar(50) NOT NULL,
  `station` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `radio`
--

INSERT INTO `radio` (`id`, `ContenName`, `url`, `Image`, `station`) VALUES
(11, 'AnimeTime', 'url1', 'imagen1.jpg', 'TokyoAnimeFM'),
(12, 'SakuraSongs', 'url2', 'imagen2.jpg', 'CherryBlossomRadio'),
(13, 'SamuraiSoul', 'url3', 'imagen3.jpg', 'BushidoBroadcast'),
(14, 'GeishaGroove', 'url4', 'imagen4.jpg', 'KyotoSounds'),
(15, 'NinjaNights', 'url5', 'imagen5.jpg', 'ShinobiStream'),
(16, 'SushiSoundtrack', 'url6', 'imagen6.jpg', 'NipponMix'),
(17, 'HarajukuHits', 'url7', 'imagen7.jpg', 'KawaiiWave'),
(18, 'SumoStyleBeats', 'url8', 'imagen8.jpg', 'YokozunaFM'),
(19, 'TeaTimeTunes', 'url9', 'imagen9.jpg', 'MatchaMelodies'),
(20, 'ZenZone', 'url10', 'imagen10.jpg', 'RisingSunRadio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recommended`
--

CREATE TABLE `recommended` (
  `UserId` int(10) NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `recommended`
--

INSERT INTO `recommended` (`UserId`, `id`) VALUES
(81177, 5),
(262664, 9),
(495407, 3),
(532861, 7),
(782996, 2),
(782996, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `userprofile`
--

CREATE TABLE `userprofile` (
  `UserId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `userprofile`
--

INSERT INTO `userprofile` (`UserId`) VALUES
(123811),
(926819),
(262664),
(532861),
(876316),
(782996),
(286033),
(81177),
(547788),
(495407);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anime`
--
ALTER TABLE `anime`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `favorites`
--
ALTER TABLE `favorites`
  ADD UNIQUE KEY `UserId` (`UserId`,`id`);

--
-- Indices de la tabla `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `queue`
--
ALTER TABLE `queue`
  ADD UNIQUE KEY `UserID` (`UserId`,`id`);

--
-- Indices de la tabla `recommended`
--
ALTER TABLE `recommended`
  ADD UNIQUE KEY `UserId` (`UserId`,`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
