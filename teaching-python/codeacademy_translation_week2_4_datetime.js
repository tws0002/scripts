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
            <div class='lesson-checkpoint__name'>datetime 模組</div>
          </div>
<div class='article__content'>
            <p>你常常會需要去追蹤事情發生的時間. 我們可以透過 Python 的 <code class='undefined'>datetime</code> 來達成.</p>

<p>我們會利用 <code class='undefined'>datetime</code> 來 print 日期和時間.</p>

          </div>
        </div>");
  }
  if(current == 2) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Getting the Current Date and Time</div>
          </div>
<div class='article__content'>
            <p>我們可以使用 <code class='undefined'>datetime.now()</code> function 來 retrieve (檢索) 現在的日期和時間.</p>

<pre><code class='python'><span class='keyword'>from</span> datetime <span class='keyword'>import</span> datetime

<span class='keyword'>print</span> datetime.now()
</code></pre>

<p>第一行 imports <code class='undefined'>datetime</code> library, 這樣才能使用它裡面的功能.</p>

<p>第二行會 print 現在的日期和時間.</p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>創造一個 variable 叫做 <code class='undefined'>now</code> ,並用它來 store (儲存) <code class='undefined'>datetime.now()</code> 的 result (結果).</li>
<li>然後 <code class='python'><span class='keyword'>print</span></code> <code class='undefined'>now</code>的 value (值).</li>
</ol>

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

                    <p>Remember that you can assign a value to the variable <code class='undefined'>now</code> using the assignment operator <code class='undefined'>=</code>.</p>

<p>For example, if you wanted to store the value 4 in now, you would type:</p>

<pre><code class='python'>now = <span class='number'>4</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");    
  }
  if(current == 3) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Extracting Information</div>
          </div>
<div class='article__content'>
            <p>有注意到 output (輸出) 的結果像這樣: <code class='css'>2013-11-25&nbsp;23<span class='pseudo'>:45</span><span class='pseudo'>:14</span><span class='class'>.317454</span></code>. 如果你不想要整個日期和時間的結果要怎麼做? </p>

<pre><code class='python'><span class='keyword'>from</span> datetime <span class='keyword'>import</span> datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day
</code></pre>

<p>你已經有了前面兩行.</p>

<p>在第三行我們單獨把 year (年) 從 <code class='undefined'>now</code> variable 中移除 並把它and store 在 <code class='undefined'>current_year</code> 中.</p>

<p>在第四和第五行, 我們從 <code class='undefined'>now</code> 中,store month (月) 和 day (日).</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>在新的一行, <code class='python'><span class='keyword'>print</span>&nbsp;now.year</code>. 記得你先指定了 <code class='undefined'>now</code> variable!</li>
<li>然後, <code class='python'><span class='keyword'>print</span></code> <code class='undefined'>now.month</code>.</li>
<li>最後, <code class='python'><span class='keyword'>print</span></code> <code class='undefined'>now.day</code>.</li>
</ol>

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

                    <p>Remember, to print out the current year, you can type:</p>

<pre><code class='python'><span class='keyword'>print</span> now.year
</code></pre>

                  </div>
                </div>
              </div>
          </div> ");
  }
  if(current == 4) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Hot Date</div>
          </div>
<div class='article__content'>
            <p>如果你想把今天的日期 print 成下面這個格式呢? <code class='perl'><span class='keyword'>m</span><span class='regexp'>月/日/年 - m/dd/yyyy</span></code>. 讓我們使用 string substitution!</p>

<pre><code class='python'><span class='keyword'>from</span> datetime <span class='keyword'>import</span> datetime
now = datetime.now()

<span class='keyword'>print</span> <span class='string'>'%s-%s-%s'</span> % (now.year, now.month, now.day)
<span class='comment'># will print: 2014-02-19</span>
</code></pre>

<p>記得 <code class='undefined'>%</code> operator 會把右側 parenthesis裡的的 string 填入 <code class='perl'><span class='variable'>%s</span></code> placeholders.</p>

<p>在上面的例子裡, 我們 print <code class='undefined'>2014-02-19</code> , 接下來要 print 的格式是: <code class='undefined'>02/19/2014</code>.</p>

          </div>
        </div>  ");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>將現在的日期 print 成這樣的格式: <code class='perl'><span class='keyword'>m</span><span class='regexp'>m/dd/yyyy</span></code>.</p>

<ol>
<li> 改變string, 使用 <code class='undefined'>/</code>  slash (斜線符號) 來區隔 <code class='perl'><span class='variable'>%s</span></code> placeholders 而不是 <code class='diff'><span class='deletion'>-</span></code> 符號.</li>
<li>重新排列 parameters (參數) 到 <code class='undefined'>%</code> operator 的右邊, 這樣你 print <code class='undefined'>now.month</code> 出來的結果, 然後才是 <code class='undefined'>now.day</code>, 然後 <code class='undefined'>now.year</code>.</li>
</ol>

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

                    <p>Don't forget to import datetime. The example code above shows you how to do so.</p>

<p>Make sure you use <code class='undefined'>now.day</code> instead of <code class='undefined'>now.date</code>. They are different things!</p>

                  </div>
                </div>
              </div>
          </div>        
");
  }
  if(current == 5) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Pretty Time</div>
          </div>
<div class='article__content'>
            <p>接下來是 hour (小時), minute(分鐘), 和 second (秒).</p>

<pre><code class='python'><span class='keyword'>from</span> datetime <span class='keyword'>import</span> datetime
now = datetime.now()

<span class='keyword'>print</span> now.hour
<span class='keyword'>print</span> now.minute
<span class='keyword'>print</span> now.second
</code></pre>

<p>在上面的例子裡, 我們 print 現在的 hour, 然後 minute, 最後是 second.</p>

<p>在這裡可以繼續使用已經 declare 的 variable <code class='undefined'>now</code> 來 print 時間.</p>

          </div>
        </div>   ");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>像上一個作業一樣, 把現在時間 print 成下面的格式: <code class='css'><span class='tag'>hh</span><span class='pseudo'>:mm</span><span class='pseudo'>:ss</span></code>.</p>

<ol>
<li>改變 string, 讓 <code class='undefined'>:</code> 符號介於 <code class='perl'><span class='variable'>%s</span></code> placeholders 之間.</li>
<li>把 month, day, year 換成 <code class='undefined'>now.hour</code>, <code class='undefined'>now.minute</code>, 和 <code class='undefined'>now.second</code>.</li>
</ol>

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

                    <p>To get the hour, you can type:</p>

<pre><code class='python'>now.hour
</code></pre>

<p>You can also use <code class='undefined'>now.minute</code> and <code class='undefined'>now.second</code>.</p>

                  </div>
                </div>
              </div>
          </div>  ");
  }
  if(current == 6) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Grand Finale</div>
          </div>
<div class='article__content'>
            <p>現在要結合剛剛的兩個練習!</p>

<pre><code class='python'><span class='keyword'>from</span> datetime <span class='keyword'>import</span> datetime
now = datetime.now()

<span class='keyword'>print</span> <span class='string'>'%s/%s/%s'</span> % (now.month, now.day, now.year)
<span class='keyword'>print</span> <span class='string'>'%s:%s:%s'</span> % (now.hour, now.minute, now.second)
</code></pre>

<p>上面的例子會 print 日期, 另一行則是時間.</p>

<p>現在要 <code class='python'><span class='keyword'>print</span></code> 成一行!</p>

          </div>
        </div>    ");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>把日期和時間一起 print 成下面的格式: <code class='perl'><span class='keyword'>m</span><span class='regexp'>m/dd/yyyy</span>&nbsp;hh:mm:ss</code>.</p>

<p>一開始先把左邊的 string 的 <code class='undefined'>%</code> operator.</p>

<ol>
<li>確定有六個 <code class='perl'><span class='variable'>%s</span></code> placeholders.</li>
<li><p>輸入 placeholders 之間的 slash, colon(冒號)和 space (空格),讓他們和上面的格式一致.</p>

<p>改變 <code class='undefined'>%</code> operator.</p> 右邊 parentheses 裡的 varaibles </li>
<li><p> 改變 variables 的順序, 符合: <code class='undefined'>now.month, now.day, now.year</code> <code class='undefined'>now.hour, now.minute, now.second</code>. 確定括號裡面包含六個 variables .</p></li>
</ol>

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

                    <p>Don't forget to <code class='java'><span class='keyword'>import</span> datetime</code>. Look at the example code above if you need help doing so.</p>

                  </div>
                </div>
              </div>
          </div>   ");
  }
  $(".is-hidden-if-is-expanded").replaceWith("<span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>");
  $(".is-shown-if-is-expanded--inline").replaceWith("<span class='is-shown-if-is-expanded--inline'><b>暗示</b></span>");  
  $(".lesson__course-name.one-line-text.js-course-name").text("Python Syntax(語法)");   
  $("p").css("font-family", "Meiryo");
  $("<style type='text/css'> body.composer{ font-family: 'Meiryo', 'Open Sans','Hevetica Neue','Helvetica',sans-serif; position: relative; overflow: hidden; width: auto; font-size: 17px; line-height: 30px;} </style>").appendTo("head");  
}

translate();
var text = document.querySelector(".lesson-left-bar");
var observer = new MutationObserver(function(mutations){
  observer.disconnect();
  translate();
  observer.observe(text, {childList: true, characterData: false, characterDataOldValue: false, subtree: true});
});
observer.observe(text, {childList: true, characterData: false, characterDataOldValue: false, subtree: true});


