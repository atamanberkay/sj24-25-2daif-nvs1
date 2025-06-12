<?php
function maxArea($height) {
    $left = 0;
    $right = count($height) - 1;
    $maxWater = 0;

    while ($left < $right) {
        $h = min($height[$left], $height[$right]);
        $w = $right - $left;
        $area = $h * $w;
        $maxWater = max($maxWater, $area);

        // Move the pointer pointing to the shorter line
        if ($height[$left] < $height[$right]) {
            $left++;
        } else {
            $right--;
        }
    }

    return $maxWater;
}

// Example usage:
echo maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]); // Output: 49
