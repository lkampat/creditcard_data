<?php
function doit(){
    echo "did it";
}
?>
--------------
hello
<html>
<body>
hello
<?php

echo "hello";


$file='test_preprocessed.csv';
$current = file_get_contents($_FILES['test_preprocessed']['tmp_name']);
file_put_contents($file, $current);


?>
</body>
<html>

