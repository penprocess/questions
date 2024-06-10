<?php
function generateNumbers($limit) {
    $numbers = [];
    for ($i = 1; $i <= $limit; $i++) {
        $numbers[] = $i;
    }
    return $numbers;
}

$numbers = generateNumbers(13);

foreach ($numbers as $number) {
    echo $number . "\n";
}
?>