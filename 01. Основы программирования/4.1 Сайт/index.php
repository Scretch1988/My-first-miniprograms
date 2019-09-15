<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css"> 
</head>
<body>

<div class="content">

<?php
	inclued_get_data "menu.php";
?>

	<h1>Личный сайт студента GeekBrains</h1>

	<div class="center">
	<img src="img/photo.png">
		<div class="box_text">
			<p><b>Добрый день</b>. Меня зовут <i>Виктор Овсянников</i>. Мне 31 год и я хочу изучить программирование чтобы в дальнейшем быть квалифицированным специалистом.</p>

			<p>В этом мне помогает IT-портал <a href="https://geekbrains.ru">GeekBrains</a></p>

			<p>На этом сайте вы сможете сыграть в несколько игр, которые я написал: <br>
			<a href="#">Главная</a>,
			<a href="#">Загадки</a>,
			<a href="#">Угадайка</a>
			</p>
		</div>
	</div>
</div>
<div class="footer">
	Copyright &copy; <? php echo date(Y);?> Viktor Ovsyannikov
<div>


</body>
</html>