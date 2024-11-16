<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q7 - Command Input</title>
</head>
<body>
    <label>Enter command: <input type="text" id="commandInput" onkeydown="executeCommand(event)"></label>
    <div id="imageContainer"></div>

    <script>
        function executeCommand(event) {
            if (event.key === 'Enter') {
                const command = document.getElementById('commandInput').value.toLowerCase();
                const img = document.createElement('img');
                if (command === 'display lion') {
                    img.src = 'lion.jpg';
                } else if (command === 'display frog') {
                    img.src = 'frog.jpg';
                } else {
                    alert('Invalid command');
                    return;
                }
                document.getElementById('imageContainer').innerHTML = '';
                document.getElementById('imageContainer').appendChild(img);
            }
        }
    </script>
</body>
</html>
