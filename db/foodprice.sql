-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-06-14 21:06:30
-- 伺服器版本： 10.4.22-MariaDB
-- PHP 版本： 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `lsa2`
--

-- --------------------------------------------------------

--
-- 資料表結構 `foodprice`
--
create database lsa2;
use lsa2;

CREATE TABLE `foodprice` (
  `id` int(11) NOT NULL,
  `foodName` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `price` int(11) NOT NULL,
  `unit` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `foodprice`
--

INSERT INTO `foodprice` (`id`, `foodName`, `price`, `unit`) VALUES
(1, '雞蛋', 41, '一斤 / 600 (公克)'),
(2, '蛋', 41, '一斤 / 600 (公克)'),
(3, '皮蛋', 19, '1 粒 (55 公克)'),
(4, '油豆腐', 43, '220 公克'),
(5, '凍豆腐', 30, '300 公克'),
(6, '豆腐', 18, '290 公克'),
(7, '嫩豆腐', 14, '300 公克'),
(8, '雞蛋豆腐', 28, '300 公克'),
(9, '雞胸', 87, '290 公克'),
(10, '雞翅', 64, '250 公克'),
(11, '雞腿', 118, '400 公克'),
(12, '豬繳肉', 79, '350 公克'),
(13, '豬里肌', 129, '200 公克'),
(14, '豬梅花', 118, '200 公克'),
(15, '豬後腿', 126, '300 公克'),
(16, '油', 55, '600 ml'),
(17, '無鹽奶油', 59, '100 公克'),
(18, '醬油', 69, '1000 ml'),
(19, '蠔油', 69, '1200 ml'),
(20, '橄欖油', 509, '1.5 ml'),
(21, '番茄醬', 40, '300 公克'),
(22, '豬', 86, '1 公斤'),
(23, '豬肉', 86, '1 公斤'),
(24, '糖', 46, '500 g'),
(25, '鹽', 18, '1 公斤'),
(26, '胡椒', 45, '30 g'),
(27, '黑胡椒', 45, '30 g'),
(28, '水', 17, '1500 ml'),
(29, '白醋', 33, '600 g'),
(30, '醋', 33, '600 ml'),
(31, '烏醋', 31, '595 ml'),
(32, '牛肉', 300, '250 g'),
(33, '太白粉', 23, '300 g'),
(34, '蒜', 27, '40 g'),
(35, '蔥', 40, '200 g'),
(36, '蝦', 169, '250 g'),
(37, '美乃滋', 115, '250 ml'),
(38, '米血', 35, '450 g'),
(39, '米', 60, '600 g'),
(40, '金針菇', 10, '200 g'),
(41, '低筋麵粉', 56, '1 kg'),
(42, '中筋麵粉', 56, '1 kg'),
(43, '高筋麵粉', 56, '1 kg'),
(44, '麵粉', 56, '1 kg');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `foodprice`
--
ALTER TABLE `foodprice`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `foodprice`
--
ALTER TABLE `foodprice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
