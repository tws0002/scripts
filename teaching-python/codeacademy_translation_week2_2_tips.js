javascript:
function translate() {
  progress = $(".lesson__show-checkpoints").text();
  current = parseInt(progress.split("/")[0]);
  $(".block-label--light-blue").text("說明");
  content = $(".article__inner")[1];
  instructions = $(".article__inner")[3];
  if(current == 1) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>美國點餐</div>
          </div>
          <div class='article__content'>
            <p>我門來實際試試Python吧.</p>

<p>你剛在美國的某家餐廳吃完飯拿到帳單:</p>

<ul>
<li><strong>飯錢</strong>: $44.50</li>
<li><strong>稅</strong>: 6.75%</li>
<li><strong>小費</strong>: 15%</li>
</ul>

<p>小費是加上稅後算出來的.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>我們先建一個 variable <code class='undefined'>meal</code> 把它設為 <code class='undefined'>44.50</code>.</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' onclick='proAdTrackImpression();' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>不要用 $  (<code class='undefined'>$</code>)—我們只要數字就好了, <code class='undefined'>44.50</code>.</p>

<p>記住設定 variable 的方法:</p>

<pre><code class='python'>variable_name = <span class='number'><span class='number'>10</span></span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>    ");
  }
  if(current == 2) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>稅</div>
          </div>
          <div class='article__content'>
            <p>Good! 我們接下來建立一個稅率 variable.</p>

<p>帳單上的稅是 6.75%. 你需要 6.75 除與 100 來得到小數點型式的百分比</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>建立 <code class='undefined'>tax</code> variable 把它設為小數點型式的 6.75%.</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' onclick='proAdTrackImpression();' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>If you want to figure out the decimal form of 6.75%, then, you have to divide 6.75 by 100, which equals 0.0675.</p>

                  </div>
                </div>
              </div>
          </div>       ");    
  }
  if(current == 3) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>小費</div>
          </div>
          <div class='article__content'>
            <p>Nice work! 餐廳服務很好所以你該留15%的小費加在餐錢加稅後.</p>

<p>我們計算總費之前我們先設小費的 variable. 我們需要小數點的百分比, 所以 15.0/100</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在<a href='javascript:void(0)' class='line-no' data-from='5' data-to=''>第 5 行</a>設 <code class='undefined'>tip</code> variable 為 15% 小數點型式 .</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' onclick='proAdTrackImpression();' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>Try doing 15.0 / 100 (or you can type <code class='undefined'>0.15</code> directly).</p>

                  </div>
                </div>
              </div>
          </div>   ");
  }
  if(current == 4) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>一行搞定</div>
          </div>
          <div class='article__content'>
            <p>Okay! 我們有三個 variable 需要用來做計算, 我們也知道一些數學 operators(數因子).</p>

<p>我們在第一課有學到怎麼重設 variable. 比如說 <code class='ini'><span class='setting'>spam = <span class='value'><span class='number'>7</span></span></span></code>, 可是我們想換一個數字試試, 像 <code class='ini'><span class='setting'>spam = <span class='value'><span class='number'>3</span></span></span></code>.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在 <a href='javascript:void(0)' class='line-no' data-from='7' data-to=''>第 7 行</a>, 重設 <code class='undefined'>meal</code> 為 自己 + 自己 * 稅. 是的你可以用本身來重設自己</p>

<p>我們這裡只計算餐費加稅.</p>

              <div class='ui-accordian ui-accordian--lesson transition--max-height' style='max-height: 42px;'>
                <div class='ui-accordian__inner'>
                  <a href='#' onclick='proAdTrackImpression();' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>Let's see: <code class='undefined'>meal * tax</code> will give you the number of tax dollars to put on your bill, and <code class='undefined'>meal</code> + that number will give you the cost of the meal + tax!</p>

<p>The interpreter will evaluate the right-hand side of the equation first. It will ask itself, 'What's <code class='undefined'>meal</code> * <code class='undefined'>tax</code>?' Once it does this and gets the result (about 3.00), it will ask itself, 'What's <code class='undefined'>meal</code> + this number?' (44.50 + about 3.00 = about 47.50.) Finally, it'll move to the left-hand side of the equation and say, 'Oh man, I should totally reassign <code class='undefined'>meal</code> (which was 44.50) to this new value of about 47.50.' And that's how <code class='undefined'>meal</code> gets reassigned!</p>

                  </div>
                </div>
              </div>
          </div>     ");
  }
  if(current == 5) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>總計</div>
          </div>
          <div class='article__content'>
            <p>現在 <code class='undefined'>meal</code> 有了餐錢加稅, 讓我們在 <a href='javascript:void(0)' class='line-no' data-from='8' data-to=''>第 8 行</a> 一個新的 variable, <code class='undefined'>total</code>, 等於新的 <code class='undefined'>meal</code> + <code class='undefined'>meal</code> * <code class='undefined'>tip</code>.</p>

<p><a href='javascript:void(0)' class='line-no' data-from='10' data-to=''>第 10 行</a> 的 code 會在 console 上印出來 total 的數值. 注意顯示出來的數值在小數點後兩位。 我們會在下一堂課學到字串格式化</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p> 在<a href='javascript:void(0)' class='line-no' data-from='8' data-to=''>第 8　行</a>　設 variable <code class='undefined'>total</code> 為 <code class='undefined'>meal</code> + <code class='undefined'>meal</code> * <code class='undefined'>tip</code> 的總合. 你現在有了你完整的餐費!</p>
          </div>        ");
  }

  $(".is-hidden-if-is-expanded").replaceWith("<span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>");
  $(".is-shown-if-is-expanded--inline").replaceWith("<span class='is-shown-if-is-expanded--inline'><b>暗示</b></span>");  
  $(".lesson__course-name.one-line-text.js-course-name").text("小費計算機");   
  $("p").css("font-family", "Meiryo");
  $("<style type='text/css'> body.composer{ font-family: 'Meiryo', 'Open Sans','Hevetica Neue','Helvetica',sans-serif; position: relative; overflow: hidden; width: auto; font-size: 17px; line-height: 22px;} </style>").appendTo("head");  
}

translate();
var text = document.querySelector(".lesson-left-bar");
var observer = new MutationObserver(function(mutations){
  observer.disconnect();
  translate();
  observer.observe(text, {childList: true, characterData: false, characterDataOldValue: false, subtree: true});
});
observer.observe(text, {childList: true, characterData: false, characterDataOldValue: false, subtree: true});


