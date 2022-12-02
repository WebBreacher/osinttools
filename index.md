BACKMOJI takes a Bitmoji ID, version (usually the number 5), and a maximum value. Press the "Grab Images!" button and your browser will make "maximum value" requests for the images of that user's Bitmoji. Those images will be displayed below.

Below are links to Griffin's and Micah's blog posts that spurred this tool to be created.
- [Griffin (Hatless1der) Glynn](https://twitter.com/hatless1der) - [https://hatless1der.com/a-snapchat-osint-tip-viewing-bitmoji-changes/](https://hatless1der.com/a-snapchat-osint-tip-viewing-bitmoji-changes/)
- [Micah (WebBreacher) Hoffman](https://twitter.com/webbreacher) - [https://webbreacher.com/2022/10/24/grabbing-old-bitmoji-outfits-with-BACKMOJI/](https://webbreacher.com/2022/10/24/grabbing-old-bitmoji-outfits-with-BACKMOJI/)

## The Bitmoji URL
Example URL: `https://images.bitmoji.com/3d/avatar/201714142-99792039934_3-s5-v1.webp`
![Bitmoji URL Broken down](/assets/images/url1.png)

## Try the Tool

<table border="1">
    <tr>
        <td>
            <p class="tooltip">Bitmoji ID <span class="tooltiptext">This is the Bitmoji ID of the user.</span></p><br>
            <input type="text" id="bid"></td>
        <td>
            <p class="tooltip">Upper<br>value <span class="tooltiptext">How many requests for images do you want to make?</span></p><br>
            <input type="text" id="upperVal" style="width: 50px;"></td>
        <td>
            <p class="tooltip">S Value <span class="tooltiptext">This is the value of the "_S#" in the URL.</span></p><br>
            <input type="text" id="sValue" style="width: 50px;" value="5" ></td>
        <td>
            <p class="tooltip">Bitmoji<br>size (px) <span class="tooltiptext">You determine the height of the resulting Bitmojis here.</span></p><br>
            <input type="text" id="avatarHeight" value="200" style="width: 70px;"></td>
    </tr>
</table>

<button type="button" onclick="getInputValue();">Grab Images!</button>

<h2>Bitmoji images below (front and side views)</h2>
<div id="all"></div>

<script type="text/javascript" style="display: none;">
    function getInputValue(){
        // Selecting the input element and get its value
        var userID = document.getElementById("bid").value;
        var sValue = document.getElementById("sValue").value;
        var upperValue = document.getElementById("upperVal").value;

        // Set Image size
        var avatarHeight = document.getElementById('avatarHeight').value;
        if(avatarHeight && (avatarHeight > 10)) {
            currentAvatarHeight = avatarHeight;
        } else {
            currentAvatarHeight = "200";
        }

        var all = document.querySelector("#all");
            const queryString = window.location.search;

        function nextImg(i) {
            var container = document.createElement('div');
            container.classList.add("avatar");
            var imgFront = document.createElement('img');
            var imgSide = document.createElement('img');
            imgFront.height = currentAvatarHeight;
            imgSide.height = currentAvatarHeight;

            var id  = userID+"_"+i+"-s"+sValue;
            imgFront.src= "https://images.bitmoji.com/3d/avatar/201714142-" + id + "-v1.webp";
            imgSide.src= "https://images.bitmoji.com/3d/avatar/582513516-" + id + "-v1.webp";
            container.appendChild(imgFront);
            container.appendChild(imgSide);
            const textNode = document.createElement("br");
            container.appendChild(textNode);

            // Make the hyperlinked text below image for front image
            const x = document.createElement("A");
            const t = document.createTextNode('Version: '+i);
            x.setAttribute("href", imgFront.src);
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
