let footer = `
<footer>
    <div class="footer-top">

    </div>

    <div class="footer">
        <div class="column footer-logo">

            <div class="flex">
                <div class="flex_icon">
                    <img src="./assets/assets/images/logo.png" alt="لوجو مكتبة الجزيرة">
                    <p>مكتبة الكترونية ومنصة ثقافية مقرها الامارات.</p>
                </div>

                <div class="footer-social">
                    <i class="fab fa-snapchat"></i>
                    <i class="fab fa-twitter"></i>
                    <i class="fab fa-instagram"></i>
                    <i class="fab fa-facebook"></i>
                </div>

            </div>


        </div>


        <div class="grid_footer">
            <div class="column">
                <h3>الأقسام</h3>
                <a href="#">الرئيسية</a>
                <a href="#">المكتبة</a>
                <a href="#">المدونة</a>
                <a href="#">من نحن</a>
                <a href="#">تواصل معنا</a>
            </div>


            <div class="column">
                <h3>روابط أخرى</h3>
                <a href="#">سياسة الإرجاع والاستبدال</a>
                <a href="#">الأسئلة الأكثر شيوعًا</a>
                <a href="#">سياسة الخصوصية</a>
            </div>

            <div class="column contact">
                <h3>تواصل معنا</h3>
                <p><i class="fas fa-phone"></i>50300046</p>
                <p><i class="fas fa-clock"></i>10:00 ص - 12:00 م</p>
                <p><i class="fas fa-envelope"></i>kuwaitbookstorenew@gmail.com</p>
            </div>

        </div>

        <div class="column books-img">
            <img src="./assets/assets/images/book.png" alt="كتب">
        </div>
    </div>

</footer>`;

let foot = document.getElementById("foot");

foot.innerHTML = footer;
