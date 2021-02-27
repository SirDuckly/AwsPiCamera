<html>
    <header>
        <?php
            session_start();
            //cd is cused so the script executes in the correct file
            $sciptPath = "cd /home/server/ && python3 /home/server/cmdWriter.py";
            function cmdFunc($camCmd , $cmdType){
                global $sciptPath;
                $cmd = $sciptPath . " " . $cmdType  . " " . $camCmd;
                $out = shell_exec($cmd);
                echo "<pre>$out</pre>";
            }
            if(isset($_POST['stop'])){
                //If stop button is pressed
                $camCmd = ($_POST['stop']);
                $cmdType = "1";
                cmdFunc($camCmd, $cmdType);
                unset($camCmd);
                unset($_POST['stop']);
            }
            if(isset($_POST['takePic'])){
                //If take picture button is pressed
                $camCmd = ($_POST['takePic']);
                $cmdType = "1";
                cmdFunc($camCmd, $cmdType);
                unset($camCmd);
                unset($_POST['takePic']);
            }
            function moveFunc($direction, $angle, $cmdType){
                global $sciptPath;
                $cmd = $sciptPath . " " . $cmdType . " " . $direction . " " . $angle;
                $out = shell_exec($cmd);
                echo "<pre>$out</pre>";
            }
            if(isset($_POST['move'])){
                //If any of the move buttons are pressed
                $direction = ($_POST['direction']);
                $angle = ($_POST['angle']);
                $cmdType = "2";
                moveFunc($direction, $angle, $cmdType);
                unset($_POST['move']);
                unset($_POST['direction']);
                unset($_POST['angle']);
            }
        ?>
    </header>
    <body>
    <h1>Pi Camera control dashboard</h1>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="90"/>
        <input type="hidden" name="direction" value="left"/>
        <input type="submit" name="move" value="Pan L 90"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="30"/>
        <input type="hidden" name="direction" value="left"/>
        <input type="submit" name="move" value="Pan L 30"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="30"/>
        <input type="hidden" name="direction" value="right"/>
        <input type="submit" name="move" value="Pan R 30"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="90"/>
        <input type="hidden" name="direction" value="right"/>
        <input type="submit" name="move" value="Pan R 90"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="30"/>
        <input type="hidden" name="direction" value="up"/>
        <input type="submit" name="move" value="Tilt up 30"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="90"/>
        <input type="hidden" name="direction" value="up"/>
        <input type="submit" name="move" value="Tilt up 90"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="30"/>
        <input type="hidden" name="direction" value="down"/>
        <input type="submit" name="move" value="Tilt down 30"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="angle" value="90"/>
        <input type="hidden" name="direction" value="down"/>
        <input type="submit" name="move" value="Tilt down 90"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="stop" value="stop"/>
        <input type="submit" name="cameraCntrl" value="Stop"/>
    </form>
    <form action="index.php" method="post">
        <input type="hidden" name="takePic" value="takePic"/>
        <input type="submit" name="cameraCntrl" value="Take picture"/>
    </form>
    </body>
</html>