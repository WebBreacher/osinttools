  <style>
    .avatar {
        width: 300px;
        display: inline-block;
    }
    img {
      height: 200px;
      width: auto;
    }
  </style>


# Backmoji - The Bitmoji Enumerator
Backmoji takes a Bitmoji ID, version (usually the number 5), and a maximum value. Press the "Grab Images!" button and your browser will make "maximum value" requests for the images of that user's Bitmoji. Those images will be displayed below.

## Blog posts that drove this page
- [Griffin (Hatless1der Glynn - https://hatless1der.com/a-snapchat-osint-tip-viewing-bitmoji-changes/](https://hatless1der.com/a-snapchat-osint-tip-viewing-bitmoji-changes/)
- [Micah (WebBreacher) Hoffman - https://webbreacher.com/2022/10/24/grabbing-old-bitmoji-outfits-with-backmoji/](https://webbreacher.com/2022/10/24/grabbing-old-bitmoji-outfits-with-backmoji/)


## Sample Data
Want to try the tool but don't have the Bitmoji data from a user profile? Use the data below.
- Sample Bimoji ID value: `99792039934`
- Version: `5`
- Upper value: `20`


## Try the Tool
- Replace the default value with your Bitmoji ID: <input type="number" id="bid" size="13" maxlength="13">
- Replace the default value with your version value: <input type="number" id="bversion" size="3" maxlength="3">
- Upper value: <input type="number" id="upperVal" size="3" maxlength="3">

    <button type="button" onclick="getInputValue();">Grab Images!</button>

    <div id="all"></div>

    <script type="text/javascript" style="display: none;">
        function getInputValue(){
            // Selecting the input element and get its value
            var userID = document.getElementById("bid").value;
            var version = document.getElementById("bversion").value;
            var upperValue = document.getElementById("upperVal").value;

           var all = document.querySelector("#all");
            const queryString = window.location.search;

            function nextImg(i) {
                var container = document.createElement('div');
                container.classList.add("avatar");
                var img = document.createElement('img');
                var id  = userID+"_"+i+"-s"+version;
                img.src= "https://images.bitmoji.com/3d/avatar/201714142-" + id + "-v1.webp";
                container.appendChild(img);
                const textNode = document.createElement("br");
                container.appendChild(textNode);

                //var p = document.createElement('p');
                //p.innerText = "<a href src=" + img.src + " target='_blank'>" + id +"</a>";
                //container.appendChild(p);

                const x = document.createElement("A");
                const t = document.createTextNode(id);
                x.setAttribute("href", img.src);
                x.setAttribute('target', '_blank');
                x.appendChild(t);
                container.appendChild(x);

                all.appendChild(container);
                console.log(i)
                if (i==upperValue) {
                    return;
                } else {
                    setTimeout(() => nextImg(i+1), 500);
                }
            }

            nextImg(0);
        }
    </script>
