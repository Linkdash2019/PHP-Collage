//Functions for basicFunctions.html
        
        function addNumbers() {
            var firstNumber = parseFloat(document.getElementById("num1").value);
            var secondNumber = parseFloat(document.getElementById("num2").value);
            var sum = firstNumber + secondNumber;
            
            alert("The sum is: " + sum);    
        }
        
        
        // add the rest of your functions below...

        function subNumbers() {
            var firstNumber = parseFloat(document.getElementById("num1").value);
            var secondNumber = parseFloat(document.getElementById("num2").value);
            var sum = firstNumber - secondNumber;
            
            alert("The factor is: " + sum);    
        }

        function clearNumbers() {
            document.getElementById("num1").value = "";
            document.getElementById("num2").value = "";

            document.getElementById("app").value = "";
            document.getElementById("food").value = "";
            document.getElementById("drink").value = "";
            document.getElementById("tip").value = "";
            document.getElementById("widget").value = "";
            document.getElementById("quantity").value = "";

        }

        function computeTotal() {
            var firstNumber = parseFloat(document.getElementById("app").value);
            var secondNumber = parseFloat(document.getElementById("food").value);
            var thirdNumber = parseFloat(document.getElementById("drink").value);
            var fourthNumber = parseFloat(document.getElementById("tip").value);
            var sum = (firstNumber + secondNumber + thirdNumber) + ((firstNumber + secondNumber + thirdNumber) * fourthNumber / 100);
            
            alert("The factor is: " + sum);
        }

        function computeOther() {
            var firstNumber = parseFloat(document.getElementById("widget").value);
            var secondNumber = parseFloat(document.getElementById("quantity").value);
            var sum = firstNumber * secondNumber;
            
            alert("The factor is: " + sum);
        }