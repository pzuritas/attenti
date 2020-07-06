<?php
$time = time();
$temp = $_POST["temp"];
$volt = $_POST["volt"];
$file = 'test.csv';
$data = $time."  - T:  ".$temp."  - V:  ".$volt;
file_put_contents($file, $data);
?>