<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q5 - Click Counters</title>
</head>
<body>
    <img src="lion.jpg" alt="Lion" onclick="countClicks('lion')">
    <img src="frog.jpg" alt="Frog" onclick="countClicks('frog')">
    <p style="color: orange;">Number of lion clicks: <span id="lionClicks">0</span></p>
    <p style="color: green;">Number of frog clicks: <span id="frogClicks">0</span></p>

    <script>
        let lionClickCount = 0;
        let frogClickCount = 0;

        function countClicks(animal) {
            if (animal === 'lion') {
                lionClickCount++;
                document.getElementById('lionClicks').innerText = lionClickCount;
            } else {
                frogClickCount++;
                document.getElementById('frogClicks').innerText = frogClickCount;
            }
        }
    </script>
</body>
</html>
