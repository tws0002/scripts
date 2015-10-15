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
                <div class='lesson-checkpoint__name'>歡迎MCD Python課程!</div>
              </div>
              <div class='article__content'>
                <p>Python 是一個很好上手的程式語言。你可以用它來寫網頁程式，遊戲，或搜尋引擎!</p>

    <p>準備好了嗎? 按SAVE&amp;Submit Code 來繼續!</p>

              </div>
            </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>準備好了嗎? 按SAVE&amp;Submit Code 來繼續!</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>暗示</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>如果介面沒有出現, 請重整介面</p>

                  </div>
                </div>
              </div>
          </div>    ");
  }
  if(current == 2) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Variables(變數)</div>
          </div>
          <div class='article__content'>
            <p>寫 web app, 遊戲, 和搜尋引擎都需要儲存和處理不同類型的數據. 這些都需要 <strong>variables(變數)</strong>. A <strong>variable(變數)</strong> 儲存數據，並給它一個特定名稱.</p>

<p>比如:</p>

<pre><code class='ini'><span class='setting'>spam = <span class='value'><span class='number'>5</span></span></span>
</code></pre>

<p>Variable <code class='undefined'>spam</code> 現在儲存了 <code class='undefined'>5</code>.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>設 variable <code class='undefined'>my_variable</code> 等於 <code class='undefined'>10</code>.</li>
<li>Click the Save &amp; Submit button to run your code.</li>
</ol>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>記住把 <code class='undefined'>my_variable</code> 放在左手邊 <code class='undefined'>=</code>, <code class='undefined'>10</code> 在右手邊.</p>

<p>你執行 code 的時候視窗會顯示 None. 這是你的 code 的結果, 不需要理會它 .</p>

                  </div>
                </div>
              </div>
          </div>");
  }

  if(current == 3) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Booleans</div>
          </div>
          <div class='article__content'>
            <p>很好! 你儲存了一個數字在一個variable. 程式裡有很多data type(資料種類), 數字只是其中之一.  另外一中是<strong>boolean(布爾 或 是非)</strong>. </p>

<p>A <strong>boolean(是非)</strong> 像一個開關, 它只有兩個數值, 就像開關一樣, boolean 只能 <code class='python'><span class='built_in'>True(是)</span></code> 或 <code class='python'><span class='built_in'>False(非)</span></code>.</p>

<p>你可以用以下的方法用variables來儲存boolean:</p>

<pre><code class='ini'><span class='setting'>a = <span class='value'><span class='keyword'>True</span></span></span>
<span class='setting'>b = <span class='value'><span class='keyword'>False</span></span></span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>請把下面3個variable設成相對的値</p>

<ol>
<li><code class='undefined'>my_int</code> 設成 <code class='undefined'>7</code></li>
<li><code class='undefined'>my_float</code> 設成 <code class='undefined'>1.23</code></li>
<li><code class='undefined'>my_bool</code> 設成 <code class='python'><span class='built_in'>True</span></code></li>
</ol>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>暗示!</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>True 和 False 記得要大寫 <code class='python'><span class='built_in'>True</span></code>!</p>

                  </div>
                </div>
              </div>
          </div>    ");
  }

  if(current == 4) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>你被重新分配了!</div>
          </div>
          <div class='article__content'>
            <p>現在你知道怎麼用variable來儲存數據了.</p>

<p>如果 <code class='ini'><span class='setting'>my_int = <span class='value'><span class='number'>7</span></span></span></code>. 你可以改變這個variable的value(數值)如此:</p>

<pre><code class='ini'><span class='setting'>my_int = <span class='value'><span class='number'>3</span></span></span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>試試看! 在編寫器裡把 <code class='undefined'>my_int</code> 的value從 <code class='undefined'>7</code> 改成 <code class='undefined'>3</code></p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>暗示!</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>你只要在第<a href='javascript:void(0)' class='line-no' data-from='8' data-to=''>line 8</a>行的等號後打 <code class='undefined'>3</code> .</p>

                  </div>
                </div>
              </div>
          </div>");    
  }

  if(current == 5) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>空格</div>
          </div>
          <div class='article__content'>
            <p>在Python裡, 空格是用來建構code的. 空格非常重要, 所以你需要很小心的用它.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>右邊code的結構有問題. 按 'Save &amp; Submit Code' 來看看會發生什麼事情.</p>

<p>你應該會看到一個錯誤訊息. 我們會在下一課給它修好!</p>

          </div>  ");    
  }

  if(current == 6) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>空白標題很空白</div>
          </div>
          <div class='article__content'>
            <p>讓我們來看看上一課的錯誤訊息:</p>

<pre><code class='undefined'>IndentationError: expected an indented block
</code></pre>

<p>這個訊息會出現如果你個空格措了. </p>

          </div>
        </div>  ");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>正確indent(縮排)右邊的code, 在第2行eggs前用4個空格來indent它, 在第3行return前用4個空格來indent它</p>

<p>Python 預設indent事4個空格.</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>你的code應該看起來如此:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>spam</span><span class='params'>()</span>:</span>
    eggs = <span class='number'>12</span>
    <span class='keyword'>return</span> eggs

<span class='keyword'>print</span> spam()
</code></pre>

                  </div>
                </div>
              </div>
          </div> ");    
  }

  if(current == 7) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Interpreter(直譯器)</div>
          </div>
          <div class='article__content'>
            <p>在頁面右上方的視窗叫做interpreter(直譯器). Interpreter 會一行一行的執行你的code, 如果遇到問題, interpreter 會顯示出錯誤訊息, 就相SpaceChem的執行一樣. </p>

<pre><code class='python'>cats = <span class='number'>3</span>
</code></pre>

<p>看看上面的範例, 我們創造一個variable叫 <code class='undefined'>cats</code> 把它的値設為 <code class='undefined'>3</code>.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>創造一個variable叫 <code class='undefined'>spam</code> 把它的値設為 <code class='python'><span class='built_in'>True</span></code>.</li>
<li>創造一個variable叫 <code class='undefined'>eggs</code> 把它的値設為 <code class='python'><span class='built_in'>False</span></code>.</li>
</ol>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>記住, 你可以用 <code class='undefined'>=</code> 來設定它的値</p>

<pre><code class='python'>example_variable = <span class='built_in'>True</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>        
");    
  }

  if(current == 8) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>單行comment(注解)</div>
          </div>
          <div class='article__content'>
            <p>你應該在之前的課程有看到 <code class='python'><span class='comment'>#</span></code> .  <code class='python'><span class='comment'>#</span></code> 符號是用來做comment(註解)的. Comment(註解) 是一行Python不會執行的字串. 它是單純給人類看的.</p>

<p>Comments 讓你的程式更容易了解. 當你回顧你的 code 或跟別人合作時, 別人可以看你的 comments 來了解你的 code 在做什麼.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>寫一個 comment 在 <a href='javascript:void(0)' class='line-no' data-from='1' data-to=''>第 1 行</a>. 注意, 開頭請用 <code class='python'><span class='comment'>#</span></code>. 寫任何東西像'請幫我加薪'.</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>你的 comment 可以像這樣:</p>

<pre><code class='python'><span class='comment'># 翻譯程式數語好麻煩</span>
</code></pre>

<p>如果你拿掉 <code class='undefined'>mysterious_variable</code>, 你有可能看到錯誤訊息, 不要裡它 </p>

                  </div>
                </div>
              </div>
          </div>");    
  }

  if(current == 9) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>多行 Comments</div>
          </div>
          <div class='article__content'>
            <p><code class='python'><span class='comment'>#</span></code> 只會 comment 一行. 雖然你可以這個樣子寫很多行 comment, 這挺麻煩的.</p>

<p>當你有很多行 comments 的時候, 你可以用 ''' 來包住整塊 comment:</p>

<pre><code class='python'><span class='string'>'''Sipping from your cup 'til it runneth over,
Holy Grail.
'''</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>寫很多行的 comment, 任何東西都可以</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>你的多行 comment 就是任何以'''開使和結尾的句子,字串!</p>

                  </div>
                </div>
              </div>
          </div>       ");    
  }

  if(current == 10) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>數學</div>
          </div>
          <div class='article__content'>
            <p>很好! 我們現在來做一些加減乘除</p>

<pre><code class='python'>addition = <span class='number'>72</span> + <span class='number'>23</span>
subtraction = <span class='number'>108</span> - <span class='number'>204</span>
multiplication = <span class='number'>108</span> * <span class='number'>0.5</span>
division = <span class='number'>108</span> / <span class='number'>9</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>設 <code class='undefined'>count_to</code> 等於兩個很大數值的總和.</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>指定 variable(變數) = value(數值) 用下面的方法</p>

<pre><code class='python'>variable_name = <span class='comment'># Add your value here!</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");    
  }

  if(current == 11) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>xx次方</div>
          </div>
          <div class='article__content'>
            <p>所有的數學都可以在計算機裡算出來, 那為什麼要用 Python? 應為 Python 可以用不只是數字的 data type(數劇類型)(比如. <strong>booleans</strong>) 和指令來創造好用的程式. 計算機只算數字! </p>

<p>我們來用次方算看看.</p>

<pre><code class='ini'><span class='setting'>eight = <span class='value'><span class='number'>2</span> ** <span class='number'>3</span></span></span>
</code></pre>

<p>上面的範例,  我們創一個新的 variable 叫 <code class='undefined'>eight</code> 把它設為 <code class='undefined'>8</code>, 或是 2 到 3 次方(2^3).</p>

<p>注意我們是用 <code class='perl'><span class='variable'>**</span></code> 而不是 <code class='undefined'>*</code> ,乘的operator(運算子).</p>

          </div>
        </div>   ");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>創一個 variable 叫 <code class='undefined'>eggs</code> 用次方來設 <code class='undefined'>eggs</code> 等於 100.</p>

<p>試試看10次方.</p>

          </div> ");
  }

  if(current == 12) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Modulo(模除)</div>
          </div>
          <div class='article__content'>
            <p>最後這個 operator <strong>modulo</strong>. <strong>Modulo</strong> 會算出相除所剩下的數. 如果你打 <code class='undefined'>3 % 2</code>, 答案是 <code class='undefined'>1</code>, 應為 3 被 2 除一次還會剩下 1.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>用 modulo 來設定 <code class='undefined'>spam</code> 等於 <code class='undefined'>1</code>. 你可以用任何數字來 modulo 剩 <code class='undefined'>1</code>.</p>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>任何偶數 <code class='undefined'>% 2</code> 會等於 1.</p>

<p>記住, 你不行用 0 來除, 會出現錯誤. <code class='undefined'>%</code>也是一樣的. <code class='undefined'>10 % 0</code> 會出現錯誤!</p>

                  </div>
                </div>
              </div>
          </div> ");    
  }

  if(current == 13) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>總結</div>
          </div>
          <div class='article__content'>
            <p>Nice work! 目前為止你學會了:</p>

<ul>
<li><strong>Variables(變數)</strong>, 它儲存 values.</li>
<li><strong>Data types(資料類型)</strong>, 像數字還有 booleans</li>
<li><strong>Whitespace(空白空間)</strong>, 分開編排</li>
<li><strong>Comments(註解)</strong>, 讓你的 code 更容易懂</li>
<li><strong>Arithmetic operations(算數)</strong>, 包含 <code class='diff'><span class='addition'>+</span></code>, <code class='diff'><span class='deletion'>-</span></code>, <code class='undefined'>*</code>, <code class='undefined'>/</code>, <code class='perl'><span class='variable'>**</span></code>, 還有 <code class='undefined'>%</code></li>
</ul>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>來個總複習吧.</p>

<ol>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='1' data-to=''>第 1 行</a>寫一個單行的 comment. 寫任何東西都可以! (確認用 <code class='python'><span class='comment'>#</span></code> 開始)</li>
<li>把 variable <code class='undefined'>monty</code> 設為 <code class='python'><span class='built_in'>True</span></code>.</li>
<li>把 variable <code class='undefined'>python</code> 設為 <code class='undefined'>1.234</code>.</li>
<li>把 variable <code class='undefined'>monty_python</code> 設為 <code class='undefined'>python</code> 平方.</li>
</ol>

              <div class='ui-accordian ui-accordian--lesson'>
                <div class='ui-accordian__inner'>
                  <a href='#' class='ui-accordian__trigger ui-media'>
                    <div class='ui-media__image new-icon--small new-icon--center new-icon--circle--blue'>?</div>
                    <div class='ui-media__main'>
                      <span class='is-hidden-if-is-expanded'><b>Stuck?</b> Get a hint!</span>
                      <span class='is-shown-if-is-expanded--inline'><b>Hint</b></span>
                    </div>
                  </a>
                  <div class='ui-accordian__content has-markdown'>

                    <p>你可以直接在 variable 上用 operators(數因子)! 記住, <code class='undefined'>python</code> 平方意思是 <code class='perl'>python <span class='variable'>**</span> <span class='number'>2</span></code>.</p>

<p>Note that the name of the variable <code class='undefined'>monty_python</code> has nothing to do with the name of the variables <code class='undefined'>monty</code> and <code class='undefined'>python</code>. We just decided to use these variable names because Python people love Monty Python's Flying Circus!</p>

                  </div>
                </div>
              </div>
          </div> ");    
  }
  $(".is-hidden-if-is-expanded").replaceWith("<span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>");
  $(".is-shown-if-is-expanded--inline").replaceWith("<span class='is-shown-if-is-expanded--inline'><b>暗示</b></span>");  
  $(".lesson__course-name.one-line-text.js-course-name").text("Python Syntax(語法)");   
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
