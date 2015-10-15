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
            <div class='lesson-checkpoint__name'>Strings(字串)</div>
          </div>
<div class='article__content'>
            <p>另一個有用的 data type (資料型態)是 <strong>string (字串)</strong>. 一個 <strong>string</strong> 包含了 letters(字母), numbers(數字), 和 symbols (符號).</p>

<pre><code class='python'>name = <span class='string'><span class='string'>'Ryan'</span></span>
age = <span class='string'><span class='string'>'19'</span></span>
food = <span class='string'><span class='string'>'cheese'</span></span>
</code></pre>

<ol>
<li>在上面這個例子, 我們創造 (Create) 了一個 Variable (變數) <code class='ruby'><span class='identifier'><span class='keymethods'>name</span></span></code> 並把它設定成字串值 <code class='undefined'>'Ryan'</code>.</li>
<li>也把 <code class='undefined'>age(年齡)</code> 設定為 <code class='undefined'>'19'</code> 還有 <code class='undefined'>food (食物)</code> 設定為 <code class='undefined'>'cheese'</code>.</li>
</ol>

<p>Strings 必須要被包含在 <strong>&quot;</strong> 符號中.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
<p>建立一個新的 Variable <code class='undefined'>brian</code> 並把它 assign 為 string <code class='undefined'>'Hello&nbsp;life!'</code>.</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#'  class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>Do you remember how to declare and assign variables in Python? If not, refresh your memory <a href='http://www.codecademy.com/courses/introduction-to-python-6WeG3/0#!/exercises/1'>here</a>!</p>

<p>There is no difference between using single quotes <code class='undefined'>'</code> and double quotes <code class='undefined'>'</code>. However, sometimes it is helpful to use one or the other. If we want to include an apostrophe in our string, it would be smart to use double quotes to create the string like <code class='undefined'>'I'm a string'</code>. If we want to use quotes in the string, we might want to create the string with single quote like <code class='undefined'>'The man screamed 'I love Python!' so that everyone could hear.'</code></p>

                  </div>
                </div>
              </div>
          </div>  ");
  }
  if(current == 2) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>練習</div>
          </div>
          <div class='article__content'>
            <p>很好, 接下來再做一些string的練習.</p>

          </div>
        </div>");
    $(instructions).replaceWith("          <div class='article__inner'>
            <p>把下列的 variables 指定成相對應的字:</p>

<ol>
<li>Set <code class='undefined'>caesar</code> to <code class='undefined'>'Graham'</code></li>
<li>Set <code class='undefined'>praline</code> to <code class='undefined'>'John'</code></li>
<li>Set <code class='undefined'>viking</code> to <code class='undefined'>'Teresa'</code></li>
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

                    <p>Make sure you use exactly the capitalization shown! Python takes things <em>very</em> literally.</p>

                  </div>
                </div>
              </div>
          </div>    ");    
  }
  if(current == 3) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Escaping characters(轉義字符)</div>
          </div>
<div class='article__content'>
            <p>有一些 character (字元) 會造成問題. 舉例來說::</p>

<pre><code class='bash'>'There's a snake <span class='keyword'>in</span> my boot!'
</code></pre>

<p>這段程式碼會 break (中斷), 因為 Python 認為 <code class='undefined'>'There's'</code> 的 ' 符號結束了這個 string. 我們可以用 backslash (符號: \\) 來解決這問題:</p>

<pre><code class='bash'>'There's a snake <span class='keyword'>in</span> my boot!'
</code></pre>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>修正 Editor (編輯器) 裡的 string!</p>

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

                    <p>You can escape the <code class='undefined'>'</code> just by adding a <code class='undefined'>\</code> before it: <code class='undefined'>'</code>.</p>

<p>There's another way to fix this problem. Can you think of it?</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 4) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>運用指數</div>
          </div>
<div class='article__content'>
            <p>做的好!</p>

<p>String 中每一個字元都會被 assign (指定) 一個數字. 這個數字被稱為 <strong>index</strong>. 參照 Editor 裡的 diagram (圖表).</p>

<pre><code class='python'>c = <span class='string'>'cats'</span>[<span class='number'>0</span>]
n = <span class='string'>'Ryan'</span>[<span class='number'>3</span>]
</code></pre>

<ol>
<li>在上面的例子, 我們創造了一個新的 variable: <code class='undefined'>c</code> 並把它設定為 <code class='undefined'>'c'</code>, 也就是<code class='undefined'>'cats'</code> 這個 string 在 index 0 位置的字元.</li>
<li>接下來我們會創造一個新的 variable: <code class='undefined'>n</code> 並設定為 <code class='undefined'>'n'</code>, <code class='undefined'>'Ryan'</code>在 index 3 的 character.</li>
</ol>

<p>在 Python 裡, index 是從 0 開始而不是從 1 開始.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在第<a href='javascript:void(0)' class='line-no' data-from='13' data-to=''>13 line(行) </a>, 把 variable  <code class='undefined'>fifth_letter</code> 指定為 string 'MONTY' 的第五個 letter (字母).</p>

<p>記得第五個字母不是在 index 5. Index 要從0開始算.</p>

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

                    <p>The letter you want is <code class='undefined'>'Y'</code>.</p>

                  </div>
                </div>
              </div>
          </div>      ");
  }
  if(current == 5) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>String methods</div>
          </div>
<div class='article__content'>
            <p>Great work! 現在我們已經知道怎麼儲存 strings, 接下來看看如何用 <strong>string method</strong>(物件(Object)本身的 Function (功能)) 去改變這些string methods.</p>

<p><strong>String methods</strong> 讓你可以對 string 做一些特定的處理.</p>

<p>接下來要講下面四種 methods:</p>

<ol>
<li><code class='undefined'>len()</code></li>
<li><code class='undefined'>lower()</code></li>
<li><code class='undefined'>upper()</code></li>
<li><code class='undefined'>str()</code></li>
</ol>

<p>讓我們從 len() 開始, 它可以取得 string 的 length (長度: character 的總數)!</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='1' data-to=''>line 1</a>, 創造一個 variable 叫做 <code class='undefined'>parrot</code> 並把它設定成 string: <code class='undefined'>'Norwegian Blue'</code>.
在 <a href='javascript:void(0)' class='line-no' data-from='2' data-to=''>line 2</a>,在 <code class='python'><span class='keyword'>print</span></code> 之後輸入 <code class='undefined'>len(parrot)</code> , 像這樣: <code class='python'><span class='keyword'>print</span> len(parrot)</code>. 輸出的結果會是 <code class='undefined'>'Norwegian Blue'</code>的字數!</li>
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

                    <p>We'll explain <code class='python'><span class='keyword'>print</span></code> in the next section!</p>

                  </div>
                </div>
              </div>
          </div>
");
  }
  if(current == 6) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>lower()</div>
          </div>
<div class='article__content'>
            <p>Well done!</p>

<p>You can use the <code class='undefined'>lower()</code> method 可以避免 string 中出現大寫. 像下面這樣使用 <code class='undefined'>lower()</code>: </p>

<pre><code class='undefined'>'Ryan'.lower()
</code></pre>

<p>結果會是: <code class='undefined'>'ryan'</code>.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在 <code class='undefined'>parrot</code> 上使用 <code class='undefined'>lower()</code> 在 editor 裡的 <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>第三行</a><code class='python'><span class='keyword'>print</span></code>) 之後.</p>

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

                    <p>Your code should look something like this:</p>

<pre><code class='python'><span class='keyword'>print</span> parrot.lower()
</code></pre>

                  </div>
                </div>
              </div>
          </div>    ");
  }
  if(current == 7) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>upper()</div>
          </div>
<div class='article__content'>
            <p>現在你的 string 全部都是 lower case (小寫)了! 有一個類似的 method 可以把整個 string 改成 upper case (大寫).</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p> 為了要把 string 裡所有的 characters都換成大寫, 在 <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a> 的<code class='python'><span class='keyword'>print</span></code> 指令之後, 在 <code class='undefined'>parrot</code> 上使用 <code class='undefined'>upper()</code></p>

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

                    <p>Use the same syntax as the previous exercise! Last time, you used:</p>

<pre><code class='python'><span class='keyword'>print</span> parrot.lower()
</code></pre>

                  </div>
                </div>
              </div>
          </div>  ");
  }
  if(current == 8) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>str()</div>
          </div>
<div class='article__content'>
            <p>接下來是 <code class='undefined'>str()</code>. <code class='undefined'>str()</code> method 把不是 strings 的轉換成 string! 舉例來說:</p>

<pre><code class='undefined'>str(2)
</code></pre>

<p>會把數字 <code class='undefined'>2</code> 轉換成 <code class='undefined'>'2'</code> 這個character.</p>

          </div>
        </div>    ");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>

<li>Create a variable <code class='undefined'>pi</code> 在 <a href='javascript:void(0)' class='line-no' data-from='4' data-to=''>line 4</a> 把它設定成 <code class='undefined'>3.14</code>.</li>
<li>在<a href='javascript:void(0)' class='line-no' data-from='5' data-to=''>line 5</a> 執行 <code class='undefined'>str(pi)</code> , 之後是 <code class='python'><span class='keyword'>print</span></code>.</li>
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

                    <p>The <code class='undefined'>str()</code> syntax is like the <code class='undefined'>len()</code> syntax:</p>

<pre><code class='python'>str(pi)
</code></pre>

                  </div>
                </div>
              </div>
          </div>    ");
  }
  if(current == 9) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Dot Notation</div>
          </div>
<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Dot Notation</div>
          </div>
          <div class='article__content'>
            <p>接下來我們看看為什麼 <code class='cpp'>len(<span class='built_in'>string</span>)</code> 和 <code class='cs'>str(<span class='keyword'>object</span>)</code>是用括號, 但是 <code class='undefined'>'String'.upper()</code> 等等的是用符號: '.' </p>

<pre><code class='python'>lion = <span class='string'>'roar'</span>
len(lion)
lion.upper()
</code></pre>

<p>使用.符號的method 只適用於 strings.</p>

<p>而 <code class='undefined'>len()</code> 和 <code class='undefined'>str()</code> 則可用於其他的 data types.</p>

          </div>
        </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>On <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a>, 使用 <code class='undefined'>len()</code> 指令, argument (引數) 則是 <code class='undefined'>ministry</code>.</li>
<li>On <a href='javascript:void(0)' class='line-no' data-from='4' data-to=''>line 4</a>, 執行 <code class='undefined'>ministry</code>'s <code class='undefined'>.upper()</code> function.</li>
</ol>

          </div> ");
  }
  if(current == 10) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Printing Strings(印列, 輸出)</div>
          </div>
          <div class='article__content'>
            <p>輸入程式碼的視窗稱為 <strong>editor</strong>.</p>

<p>右上角是 <strong>console</strong> , 會顯示你程式碼執行的結果.</p>

<p><code class='python'><span class='keyword'>print</span></code> 會把你的程式碼直接顯示在 console 裡面.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在 Console 裡 Print 'Monty Python'.</p>

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

                    <p>The syntax looks like this:</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'Your string goes here'</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>   ");
  }
  if(current == 11) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Printing Variables(印列, 輸出)</div>
          </div>
<div class='article__content'>
            <p>現在我們已經 Print 過 strings 了, 現在要 print variables</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>Declare (宣告) 一個叫做 <code class='undefined'>the_machine_goes</code> 的 variable, 並 assign 它為 string: <code class='undefined'>'Ping!'</code>, (在 <a href='javascript:void(0)' class='line-no' data-from='5' data-to=''>line 5</a>).</li>
<li>在<a href='javascript:void(0)' class='line-no' data-from='6' data-to=''>line 6</a> print <code class='undefined'>the_machine_goes</code>.</li>
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

                    <p>Make sure you're setting your variable like this:</p>

<pre><code class='python'>the_machine_goes = <span class='string'>'Ping!'</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 12) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>String Concatenation(字串接合)</div>
          </div>
<div class='article__content'>
            <p>現在要結合運用 strings 和 arithmetic operators (算術運算)!</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'Life '</span> + <span class='string'>'of '</span> + <span class='string'>'Brian'</span>
</code></pre>

<p>這會 print 出 <code class='undefined'>Life of Brian</code>.</p>

<p> 在 strings 中使用 <code class='diff'><span class='addition'>+</span></code> 號這個 operator (運算子) ,會把 strings 全部 add (加, 連結)頭尾相連接在一起 ' . 有注意到 ' 符號之間有空格嗎 (在<code class='undefined'>Life</code> 和 <code class='undefined'>of</code> 之後), 這樣接起來後,因為字和字之間有空格, 才會看起來像三個字而不是一個.</p>

<p>像這樣把 string 接起來叫做 <strong>concatenation</strong>. 接下來試看看把 string concatenate 在一起!</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>接下來要 print  <code class='undefined'>'Spam&nbsp;'</code>, <code class='undefined'>'和 &nbsp;'</code>, <code class='undefined'>'eggs'</code> 接在一起 (在<a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a>), 就像上述的例子一樣.</p>

<p>確定你的字和字之間有空格: <code class='undefined'>'Spam&nbsp;'</code> and <code class='undefined'>'and '</code>.</p>

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

                    <p>Make sure you include the spaces and use the correct capitalization.</p>

                  </div>
                </div>
              </div>
          </div> ");
  }
  if(current == 13) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>硬是轉成 string</div>
          </div>
<div class='article__content'>
            <p>有時候你需要把 strings 和非string 的資料連接在一起. 這時候要先把非string的資料轉換成string.</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'I have '</span> + str(<span class='number'>2</span>) + <span class='string'>' coconuts!'</span>
</code></pre>

<p>這會 print <code class='undefined'>I have 2 coconuts!</code>.</p>

<p><code class='undefined'>str()</code> method 會把非 string 的資料轉換成 string . 在上面的例子裡,你把數字 <code class='undefined'>2</code> 轉換成 string ,然後 concatenate 這兩個 strings.</p>

<p>自己試看看!</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>直接執行上面的程式碼會得到錯誤訊息!</li>
<li>使用 <code class='undefined'>str()</code> ,來把 <code class='undefined'>3.14</code> 轉換成 string. 然後在執行一次.</li>
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

                    <p>The code to turn the number <code class='undefined'>2</code> into a string is <code class='undefined'>str(2)</code>.</p>

<p>Can you convert the number <code class='undefined'>3.14</code> into a string?</p>

                  </div>
                </div>
              </div>
          </div>  ");
  }
  if(current == 14) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>String 編排用 %, Part 1</div>
          </div>
<div class='article__content'>
            <p>當你要 print 一個 date type 是 string 的 variable, 除了 concatenate 以外還有更好的方法.</p>

<pre><code class='python'>name = <span class='string'>'Mike'</span>
<span class='keyword'>print</span> <span class='string'>'Hello %s'</span> % (name)
</code></pre>

<p> 放在 string 之後的 <code class='undefined'>%</code> percent(百分比) operator, 可以用來 combine (結合) string 和 variables. <code class='undefined'>%</code> operator 會把 strings裡的 <code class='perl'><span class='variable'>%s</span></code> 換成後面的 string variable.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>看看 editor 裡面的程式碼, 確定了解之後,按下面的 save and submit.</p>

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

                    <p>As of Python 2.6 there is a new way to do dynamic string formatting. There is now a string method called <code class='perl'>.<span class='keyword'>format</span></code> which is more advanced than using <code class='undefined'>%</code>. The reason we don't focus on this method at Codecademy (at least for now) is that it will not work in older versions of Python and thus its use is discouraged in some settings. Here's a quick explanation.</p>

<p><code class='perl'>.<span class='keyword'>format</span></code> allows you to set values and then replace those values in the string. It uses curley braces <code class='undefined'>{some_name}</code> with a variable name inside. Then the method sets those variables as arguments. It also supports many more features than using <code class='undefined'>%</code>. It's easiest to explain using examples:</p>

<pre><code class='python'><span class='string'>'I am a {type}'</span>.format(type=<span class='string'>'string'</span>)
my_name = <span class='string'>'Michael'</span>
<span class='string'>'Hello, my name is {name}'</span>.format(name=my_name)
</code></pre>

<p>There are many other great uses and you can check out the Python documentation for more <a href='http://docs.python.org/2/library/stdtypes.html#str.format'>here</a>, <a href='http://docs.python.org/3/library/string.html#string-formatting'>here</a> and <a href='http://www.python.org/dev/peps/pep-3101/'>here</a>.</p>

                  </div>
                </div>
              </div>
          </div>   ");
  }
  if(current == 15) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>String 編排用 %, Part 2</div>
          </div>
<div class='article__content'>
            <p>記住, 我們用 <code class='undefined'>%</code> operator 來把 <code class='perl'><span class='variable'>%s</span></code> placeholders(佔位符) 換成 parentheses (括號)裡的 variables.</p>

<pre><code class='python'>name = <span class='string'>'Mike'</span>
<span class='keyword'>print</span> <span class='string'>'Hello %s'</span> % (name)
</code></pre>

<p>括號裡需要和 <code class='perl'><span class='variable'>%s</span></code> 相同數量的 variables:</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'The %s who %s %s!'</span> % (<span class='string'>'Knights'</span>, <span class='string'>'say'</span>, <span class='string'>'Ni'</span>)
<span class='comment'># This will print 'The Knights who say Ni!'</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>接下來要把 <code class='undefined'>___</code> 替換掉!</p>

<ol>
<li>在String裡面, 把三個 <code class='undefined'>___</code> 換成 <code class='perl'><span class='variable'>%s</span></code>.</li>
<li>在 string 之後但是在三個 variables之前, 把最後一個 <code class='undefined'>___</code> 換成 <code class='undefined'>%</code>.</li>
<li>按 <em>Save &amp; Submit Code</em>.</li>
<li>回答彈出(pop up)視窗的問題! 把你的回答輸入視窗並按 Enter.</li>
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

                    <p>Remember, the syntax is:</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'%s'</span> % (string_variable)
</code></pre>

<p>Are you stuck with a spinning gear and it feels like your code is frozen? That's because the code is asking you three questions! Click inside the console window, type in your name, and then press Enter (or Return).</p>

<p>The <code class='undefined'>\</code> character on <a href='javascript:void(0)' class='line-no' data-from='5' data-to=''>line 5</a> is a <em>continuation marker</em>. It simply tells Python that <a href='javascript:void(0)' class='line-no' data-from='5' data-to=''>line 5</a> continues onto <a href='javascript:void(0)' class='line-no' data-from='6' data-to=''>line 6</a>.</p>

                  </div>
                </div>
              </div>
          </div>   ");
  }
  if(current == 16) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>總複習</div>
          </div>
<div class='article__content'>
            <p>你已經學到了:</p>

<p>三種創造 strings 的方法</p>

<pre><code class='python'><span class='string'>'Alpha'</span>
<span class='string'>'Bravo'</span>
str(<span class='number'>3</span>)
</code></pre>

<p>String methods</p>

<pre><code class='python'>len(<span class='string'>'Charlie'</span>)
<span class='string'>'Delta'</span>.upper()
<span class='string'>'Echo'</span>.lower()
</code></pre>

<p>Printing a string</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'Foxtrot'</span>
</code></pre>

<p>進階的 printing 技巧</p>

<pre><code class='python'>g = <span class='string'>'Golf'</span>
h = <span class='string'>'Hotel'</span>
<span class='keyword'>print</span> <span class='string'>'%s, %s'</span> % (g, h)
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>全部統整在一起</p>

<ol>
<li>On <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a>, 創造一個 variable <code class='undefined'>my_string</code> 把它的值設定成你想要的.</li>
<li>On <a href='javascript:void(0)' class='line-no' data-from='4' data-to=''>line 4</a>, <code class='python'><span class='keyword'>print</span></code> the length of <code class='undefined'>my_string</code>.</li>
<li>On <a href='javascript:void(0)' class='line-no' data-from='5' data-to=''>line 5</a>, <code class='python'><span class='keyword'>print</span></code> the <code class='undefined'>.upper()</code> (大寫 version (版本)) 的 <code class='undefined'>my_string</code>.</li>
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

                    <p>You can <code class='python'><span class='keyword'>print</span></code> a variable with a method all on one line, like so: <code class='python'><span class='keyword'>print</span> my_variable.upper()</code>.</p>

                  </div>
                </div>
              </div>
          </div>
        ");
  }
  $(".is-hidden-if-is-expanded").replaceWith("<span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>");
  $(".is-shown-if-is-expanded--inline").replaceWith("<span class='is-shown-if-is-expanded--inline'><b>暗示</b></span>");  
  $(".lesson__course-name.one-line-text.js-course-name").text("String(字串)和Console(控制台)輸出");   
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