<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
</head>
<body>
<?php
function ggt($a, $b) {
    return $b == 0 ? $a : ggt($b, $a % $b);
}

function kuerzen($z, $n) {
    $ggt = ggt($z, $n);
    return [$z / $ggt, $n / $ggt];
}

function add_fractions($frac1, $frac2) {
    list($z1, $n1) = explode('/', $frac1);
    list($z2, $n2) = explode('/', $frac2);

    // Gemeinsamen Nenner finden
    $nenner = $n1 * $n2;
    $zaehler = $z1 * $n2 + $z2 * $n1;

    // Kürzen
    list($z, $n) = kuerzen($zaehler, $nenner);

    // Gemischte Zahl berechnen
    $ganz = intdiv($z, $n);
    $rest = $z % $n;

    if ($ganz > 0 && $rest > 0) {
        return "$ganz $rest/$n";
    } elseif ($ganz > 0) {
        return "$ganz";
    } else {
        return "$z/$n";
    }
}

// Beispiel
echo add_fractions("1/2", "3/4");  // Ausgabe: 1 1/4
?>

</body>
</html>