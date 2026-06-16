function compute() {
    if (window.confirm("Are you sure you want to continue?")) {
        
        let amount = document.getElementById("quantity").value;

        if (selected == "NES") {
            amount = amount * 300;
        }
        else if (selected == "SNES") {
            amount = amount * 350;
        }
        else if (selected == "N64") {
            amount = amount * 200;
        }
        else if (selected == "GameCube") {
            amount = amount * 180;
        }
        else {
            alert("An error has occurred, please try again.");
            alert(document.getElementById("itemImg").src);
            return;
        }

        if (amount > 0) {
            popup = window.open("", "popupWindow", "width=500,height=300");
            popup.document.write(`
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Receipt</title>
                </head>
                    <body>
                        <h1>Total cost: $${amount}</h1>
                        <br>
                        <h3>You bought ${document.getElementById("quantity").value} ${selected}(s)</h3>
                    </body>
                </html>
                <style>
                    body, html {
                        height: 100%;
                        margin: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        flex-direction: column;
                    }
                </style>
            `);
            popup.document.close();
        }
        else {
            popup = window.open("", "popupWindow", "width=600,height=300");
            popup.document.write(`
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Error Report</title>
                </head>
                    <body>
                        <h1>Error: Please enter a valid amount</h1>
                    </body>
                </html>
                <style>
                    body, html {
                        height: 100%;
                        margin: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        flex-direction: column;
                    }
                </style>
            `);
            popup.document.close();
        }
    }
    else {
        popup = window.open("", "popupWindow", "width=600,height=300");
        popup.document.write(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Error Report</title>
            </head>
                <body>
                    <h1>Purchase Canceled</h1>
                </body>
            </html>
            <style>
                body, html {
                    height: 100%;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                }
            </style>
        `);
        popup.document.close();
    }
}

function changeText(whoMoved) {
    if (whoMoved === "1") {
        document.getElementById("itemDesc").innerText = "The Nintendo Entertainment System (NES for short) is the first home console released by Nintendo in 1985. Featuring classics like Super Mario Bros, The Legend of Zelda, and Metroid.";
        document.getElementById("itemImg").src = "img/NES.png";
        selected = "NES";
    }
    if (whoMoved === "2") {
        document.getElementById("itemDesc").innerText = "The Super Nintendo Entertainment System (SNES for short) is the second home console released by Nintendo in 1990. With a more comfortable controller and higher resolution games, fun goes all over the place!";
        document.getElementById("itemImg").src = "img/SNES.jpg";
        selected = "SNES";
    }
    if (whoMoved === "3") {
        document.getElementById("itemDesc").innerText = "The Nintendo 64, the third home console and first console released by Nintendo to feature 3D. It has 3D classics such as Mario 64, Kirby 64, and The Legend of Zelda: Ocarina of Time. Just don't get motion sick... ";
        document.getElementById("itemImg").src = "img/N64.png";
        selected = "N64";
    }
    if (whoMoved === "4") {
        document.getElementById("itemDesc").innerText = "The Nintendo GameCube, the fourth home console released by Nintendo in 2001. Being slightly portable with its handle, better graphics, and one of the best controllers. The GameCube had games such as Super Smash Bros, Mario Kart Double Dash, and The Legend of Zelda: Wind Waker.";
        document.getElementById("itemImg").src = "img/GameCube.jpg";
        selected = "GameCube";
    }
}

document.querySelector(`input[name="button"][value="1"]`).checked = true;
document.getElementById("quantity").value = '';
changeText("1");