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
            <div class='lesson-checkpoint__name'>What Good are Functions?</div>
          </div>
          <div class='article__content'>
            <p>你可能有想過在某些狀況下,可以在只更動幾個數值的情況下,重複使用某些程式碼. 與其重寫整段程式. define 一個 <strong>function</strong> 會是比較乾淨的做法, 之後也可以重複使用.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>Check editor 裡面的程式碼. 如果你之前有完成 [Tip Calculator][1] project, 你會記得有在一段程式碼裡面計算稅金和小費. 在這裡我們 <code class='python'><span class='keyword'>def</span></code>ined 兩個function: <code class='undefined'>tax</code>,用來計算帳單的稅金, 還有 <code class='undefined'>tip</code>, 用來計算小費.</p>

<p>先大概看一下妳可以理解多少.</p>

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

                    <p><a href='http://www.codecademy.com/courses/python-beginner-sRXwR/3#!/exercises/2'>Remember</a> how we used <code class='perl'><span class='variable'>%s</span></code> to print strings? We can use <code class='perl'><span class='variable'>%f</span></code> to print floats! (That is, numbers with decimals in them.)</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 2) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Function Junction</div>
          </div>
          <div class='article__content'>
            <p>Functions 由三個元件組成:</p>

<ol>
<li><p>The <strong>header</strong>, 包含了 <code class='python'><span class='keyword'>def</span></code> keyword, function的名稱, 還有功能所需的 <strong>parameters (參數)</strong>. 例:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>hello_world</span><span class='params'>()</span>:</span> // There are no parameters
</code></pre></li>
<li><p>一個可有可無的 <strong>comment(評論)</strong>, 用來解釋這個功能的用途.</p>

<pre><code class='python'><span class='string'>'''Prints 'Hello World!' to the console.'''</span>
</code></pre></li>
<li><p>The <strong>body</strong>, 也就是這個 function 會執行的 procedures(程序). The body 就像 conditional statements一樣會 <em>indented(縮排)</em>.</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'Hello World!'</span>
</code></pre></li>
</ol>

<p>這裡是整個 function 放在一起的樣子:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>hello_world</span><span class='params'>()</span>:</span>
    <span class='string'>'''Prints 'Hello World!' to the console.'''</span>
    <span class='keyword'>print</span> <span class='string'>'Hello World!'</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>自己創造一個 function, <code class='undefined'>spam</code>, 這個 fuinction 會 <code class='python'><span class='keyword'>print</span></code> <code class='undefined'>'Eggs!'</code> 到 console 螢幕上. 不要忘記加上 comment (用三個quotes把它包起來!).</p>

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

                    <p>If you're stuck, look closely at the example function syntax in the instructional text. Remember: whitespace counts in Python!</p>

                  </div>
                </div>
              </div>
          </div>");    
  }
  if(current == 3) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Call and Response</div>
          </div>
          <div class='article__content'>
            <p>在 define 一個 function之後, 它一定要被 <strong>called</strong> 才會 implemented (執行) . 在前面的練習裡, 在最後一行的 <code class='undefined'>spam()</code> 告訴程式去找到 <code class='undefined'>spam</code> 並 call 這個 function 去執行.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>我們已經設定好一個 function, <code class='undefined'>square</code>. 在 <a href='javascript:void(0)' class='line-no' data-from='9' data-to=''>line 9</a>!</p> call 這個 function, 並以 <code class='undefined'>10</code> 做為它的 argument (把 <code class='undefined'>10</code> 輸入到 <code class='undefined'>square()</code> 的 parentheses 之中 ) 

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

                    <p>Remember when we called <code class='undefined'>spam</code> in the previous exercise, like this: <code class='undefined'>spam()</code>? You can do the same here with <code class='undefined'>square()</code>, only you'll need to put <code class='undefined'>10</code> in between the parentheses so <code class='undefined'>square</code> knows what number to... well, square.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 4) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Parameters and Arguments</div>
          </div>
          <div class='article__content'>
            <p>讓我們重新檢視在上個練習中 define 的 <code class='undefined'>square</code> function:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>square</span><span class='params'>(n)</span>:</span>
</code></pre>

<p><code class='undefined'>n</code> 是 <code class='undefined'>square</code> 的 <strong>parameter</strong> . parameter 就像是 variable 的 名稱, 讓你可以把 <strong>argument</strong>輸入到 function裡面. 在上個例子裡, 我們用 argument <code class='undefined'>10</code> call  <code class='undefined'>square</code> function, . 在這情況下, 這個 function 執行的時候 <code class='undefined'>n</code> 就代表 <code class='undefined'>10</code>.</p>

<p>一個功能可以包含無限多的 parameters, 但當你call 一個 function時, 一般來說需要輸入一樣數量的 arguments.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>看看 editor裡的 function: <code class='undefined'>power</code>. 它需要兩個 arguments, 一個是 base (基數), 另一個是 exponent (指數), 結果是 base 以第二個為指數算出次方 . 現在因為缺乏paremeters而無法運作.</p>

<p>把 <code class='undefined'>___</code>s 換成 parameters <code class='cs'><span class='keyword'>base</span></code> 和 <code class='undefined'>exponent</code> 並以 <code class='undefined'>37</code> 做為 <code class='cs'><span class='keyword'>base</span></code>, 以<code class='undefined'>4</code>做為<code class='undefined'>power</code>, 執行 <code class='undefined'>power</code> .</p>

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

                    <p>Make sure to include the parameters <code class='cs'><span class='keyword'>base</span></code> and <code class='undefined'>exponent</code> between the parentheses on <a href='javascript:void(0)' class='line-no' data-from='1' data-to=''>line 1</a>, and the arguments <code class='undefined'>37</code> and <code class='undefined'>4</code> between the parentheses on <a href='javascript:void(0)' class='line-no' data-from='5' data-to=''>line 5</a>. Your parameters and arguments need to be separated by a comma, like this: <code class='cs'>(<span class='keyword'>base</span>, exponent)</code>.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 5) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Functions Calling Functions</div>
          </div>
          <div class='article__content'>
            <p>除了上一個章節講到那些功能, Function 裡面也可以直接 call 另一個 function:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>fun_one</span><span class='params'>(n)</span>:</span>
    <span class='keyword'>return</span> n * <span class='number'>5</span>

<span class='function'><span class='keyword'>def</span> <span class='title'>fun_two</span><span class='params'>(m)</span>:</span>
    <span class='keyword'>return</span> fun_one(m) + <span class='number'>7</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>讓我們看看 editor 裡面的兩個 function: <code class='undefined'>one_good_turn</code>, (這功能把 argument + <code class='undefined'>1</code> return) 還有另一個function: <code class='undefined'>deserves_another</code> (這功能把 argument + <code class='undefined'>2</code>).</p>

<p>改變 <code class='undefined'>deserves_another</code> 的功能內容, 讓她 return 的是 <code class='undefined'>one_good_turn</code> 的 ouput 加 <code class='undefined'>2</code>.</p>

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

                    <p>The <code class='undefined'>n</code> in the body of <code class='undefined'>deserves_another</code> should be replaced by a call to the function <code class='undefined'>one_good_turn(n)</code>.</p>

                  </div>
                </div>
              </div>
          </div>
");
  }
  if(current == 6) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Practice Makes Perfect</div>
          </div>
          <div class='article__content'>
            <p>接下來創造更多的功能.</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>shout</span><span class='params'>(phrase)</span>:</span>
    <span class='keyword'>if</span> phrase == phrase.upper():
        <span class='keyword'>return</span> <span class='string'>'YOU'RE SHOUTING!'</span>
    <span class='keyword'>else</span>:
        <span class='keyword'>return</span> <span class='string'>'Can you speak up?'</span>

shout(<span class='string'>'I'M INTERESTED IN SHOUTING'</span>)
</code></pre>

<p>上面的例子只是用來幫助你理解 function 的結構.</p>

<p>define function 的那行最後面要加一個冒號!</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>首先, <code class='python'><span class='keyword'>def</span></code> 一個 function 叫做 <code class='undefined'>cube</code> , 它的 parameter 叫做 <code class='undefined'>number</code>. 不要忘記 parentheses 和 colon!</li>
<li>讓這個 function <code class='java'><span class='keyword'>return</span></code> <code class='undefined'>number</code> 的三次方 .</li>
<li>Define 第二個 function 叫做 <code class='undefined'>by_three</code>, 它的 parameter 叫做 <code class='undefined'>number</code>.</li>
<li><code class='java'><span class='keyword'>if</span></code> 如果 number 可以被 3 整除, <code class='undefined'>by_three</code> 會 call <code class='undefined'>cube(number)</code> 這個function, 並 return 和 <code class='undefined'>cube(number)</code> 相同的結果. 否則的話, <code class='undefined'>by_three</code> 應該要 <code class='python'><span class='keyword'>return</span> <span class='built_in'>False</span></code>.</li>
</ol>

<p>不要忘了 <code class='java'><span class='keyword'>if</span></code> 和 <code class='java'><span class='keyword'>else</span></code> statements 結尾處需要 <code class='undefined'>:</code>!</p>

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

                    <pre><code class='python'><span class='keyword'>if</span> n % <span class='number'>3</span> == <span class='number'>0</span>:
    <span class='keyword'>print</span> <span class='string'>'n is divisible by 3'</span>
<span class='keyword'>else</span>:
    <span class='keyword'>print</span> <span class='string'>'n is not'</span>
</code></pre>

<p>Make sure both functions <code class='java'><span class='keyword'>return</span></code> their values rather than <code class='python'><span class='keyword'>print</span></code>ing them.</p>

<p><em>Both</em> branches of the <code class='java'><span class='keyword'>if</span></code>/<code class='java'><span class='keyword'>else</span></code> statement in <code class='undefined'>by_three</code> need to have <code class='java'><span class='keyword'>return</span></code> statements in them (that's three <code class='java'><span class='keyword'>return</span></code>s total, two for <code class='undefined'>by_three</code> and one for <code class='undefined'>cube</code>).</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 7) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>I Know Kung Fu</div>
          </div>
          <div class='article__content'>
            <p>還記得 <code class='java'><span class='keyword'>import</span> <span class='keyword'>這個</span></code> 第一堂課的內容嗎? 講的是 <strong>import</strong>ing a <strong>module</strong>. 一個 module 是一個檔案, 裡面包含了 variables 和 functions, 只要 import 之後就可以使用.</p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在我們進行華麗的 importing 之前, 先看看 Python 開平方根的功能. 在 editor <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a> , print sqrt(25)</p>

<pre><code class='python'><span class='keyword'>print</span> sqrt(<span class='number'>25</span>)
</code></pre>

<p>結果應該是五.</p>

          </div>");
  }
  if(current == 8) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Generic Imports</div>
          </div>
          <div class='article__content'>
            <p>有看到剛剛的錯誤訊息嗎?'NameError: name 'sqrt' is not defined.', Python 現在還不知道什麼是 square roots.</p>

<p>有一個 Python Module叫做 <code class='undefined'>math</code> 它包含了許多有用的 variables 和 functions, <code class='perl'><span class='keyword'>sqrt</span>()</code> 也是其中之一. 為了要可以存取 <code class='undefined'>math</code> 裡的功能, 你需要做的就是 <code class='java'><span class='keyword'>import</span></code>. 當你直接 import 一個 module, 叫做 <strong>generic import</strong>.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在這裡需要做兩件事:</p>

<ol>
<li>在 editor <a href='javascript:void(0)' class='line-no' data-from='2' data-to=''>line 2</a> 輸入 <code class='java'><span class='keyword'>import</span> math</code>.</li>
<li>在 <code class='perl'><span class='keyword'>sqrt</span>() 之前插入 <code class='undefined'>math.</code></code>, 像這樣: <code class='perl'>math.<span class='keyword'>sqrt</span>()</code>. 這告訴 Python, 不只要 <code class='java'><span class='keyword'>import</span> math</code>, 還要從 <code class='undefined'>math</code> module中取得 <code class='perl'><span class='keyword'>sqrt</span>() function</code>.</li>
</ol>

<p>Then hit Save &amp; Submit to see what Python now knows.</p>

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

                    <p>Make sure you <code class='java'><span class='keyword'>import</span> math</code> (no colons or anything like that), and make sure you ask Python to <code class='perl'><span class='keyword'>print</span> math.<span class='keyword'>sqrt</span>(<span class='number'>25</span>)</code>.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 9) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Function Imports</div>
          </div>
          <div class='article__content'>
            <p>很好, 現在 Python 知道要怎麼計算 square root 了.</p>

<p>然而, 我們其實只需要 <code class='perl'><span class='keyword'>sqrt</span></code> function, 一直重複打 <code class='perl'>math.<span class='keyword'>sqrt</span>()</code>會令人感到很挫折.</p>

<p>我們可以從一個 module裡面, 只 import 需要的 variables 或是 functions. 這麼做叫做 <strong>function import</strong>, 這是透過 <code class='python'><span class='keyword'>from</span></code> 這個關鍵字來完成的:</p>

<pre><code class='python'><span class='keyword'>from</span> module <span class='keyword'>import</span> function
</code></pre>

<p>現在你可以只輸入 <code class='perl'><span class='keyword'>sqrt</span>()</code> 就可以計算平方根, 不用在打 <code class='perl'>math.<span class='keyword'>sqrt</span>()</code>!</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>讓我們從<code class='undefined'>math</code> module中, 只 import  <code class='perl'><span class='keyword'>sqrt</span></code> function. (Import 的指令是 <code class='python'><span class='keyword'>from</span> math <span class='keyword'>import</span> sqrt</code>, 不需要在 <code class='perl'><span class='keyword'>sqrt</span></code> 之後輸入 <code class='undefined'>()</code>  </p>

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

                    <p>Remember: <code class='python'><span class='keyword'>from</span> module <span class='keyword'>import</span> function</code>! (Don't include the parentheses here—just the function name, <em>e.g.</em> <code class='perl'><span class='keyword'>sqrt</span></code>.)</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 10) {
    $(content).replaceWith("
<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Universal Imports</div>
          </div>
          <div class='article__content'>
            <p></p>

<p>如果我們同時想要 module 裡所有的 variables 和 functions 卻又不想一直輸入 <code class='undefined'>math.</code>呢?</p>

<p><strong>Universal import</strong> 可以解決這個問題. 語法如下:</p>

<pre><code class='python'><span class='keyword'>from</span> module <span class='keyword'>import</span> *
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在 <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a> 執行 <code class='python'><span class='keyword'>from</span> module <span class='keyword'>import</span> *</code> 來 import <code class='undefined'>math</code> module 裡的所有物件.</p>

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

                    <p>Just like this: <code class='python'><span class='keyword'>from</span> math <span class='keyword'>import</span> *</code></p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 11) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Here Be Dragons</div>
          </div>
          <div class='article__content'>
            <p>Universal imports 看起來很方便, 但是最好不要這樣做, 因為他們會直接佔用你程式裡的 variable 和 function 名稱, 而不是在 module 自己的名稱之下.</p>

<p>如果你有一個自己寫,而且命名為 <code class='perl'><span class='keyword'>sqrt</span></code> 的 function, 然後你 <code class='java'><span class='keyword'>import</span> math</code>, 那不會影響到你的 function: 你的 <code class='perl'><span class='keyword'>sqrt</span></code> 就是叫做 sqrt , 而 math module 裡的 sqrt 則是叫做 <code class='perl'>math.<span class='keyword'>sqrt</span></code>. 如果你是用 <code class='python'><span class='keyword'>from</span> math <span class='keyword'>import</span> *</code>, 兩個 function 會共用同一個名稱.</p>

<p>即使你自己定義的 functions 和 variables 沒有和 imported modules 衝突, 如果你同時從好幾個 modules <code class='java'><span class='keyword'>import</span> *</code> , 你會無法判斷 variables 和 functions 到底是哪個module的.</p>

<p>因為這些原因, 最好還是用 <code class='ruby'><span class='identifier'>import</span> <span class='class'><span class='keyword'>module</span></span></code> 並輸入 <code class='ruby'><span class='class'><span class='keyword'>module</span>.<span class='title'>name</span></span></code> 或是只 <code class='java'><span class='keyword'>import</span></code> 需要的特定 variables 或是 functions.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>Editor 裡的程式碼可以讓你看到 <code class='undefined'>math</code> module 裡提供的所有物件.</p>

<p>Click Save &amp; Submit Code to check it out (you'll see <code class='perl'><span class='keyword'>sqrt</span></code>, along with some other useful things like <code class='undefined'>pi</code>, <code class='undefined'>factorial</code>, and <a href='http://en.wikipedia.org/wiki/Trigonometry'>trigonometric functions</a>).</p>

          </div>");
  }
  if(current == 12) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>On Beyond Strings</div>
          </div>
          <div class='article__content'>
            <p>現在你已經了解 functions 是什麼, 還有如何 import modules, 接下來要看的是 Python 內建的 function (不需要import 任何 module!).</p>

<p>你已經了解了一些我們曾經用在 strings 上的功能, 像是 <code class='undefined'>.upper()</code>, <code class='undefined'>.lower()</code>, <code class='undefined'>str()</code>, and <code class='undefined'>len()</code>. 它們用在 strings 上很好用,但如果要分析資料的時候呢?</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>你覺得 editor 裡面的 code 可以幹嘛? Click Save &amp; Submit Code when you think you have an idea.</p>

          </div>");
  }
  if(current == 13) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>max()</div>
          </div>
          <div class='article__content'>
            <p><code class='ruby'><span class='identifier'><span class='keymethods'>max</span></span>()</code> function 會 return 它收到的所有 argument 裡面最大的. ('最大' 有時候定義有點奇怪,所以最好是只把 <code class='ruby'><span class='identifier'><span class='keymethods'>max</span></span>()</code> 用在 integers (整數) 和  floats (小數)上, 得到的結果會最直接.</p>

<p>舉例來說, <code class='ruby'><span class='identifier'><span class='keymethods'>max</span></span>(<span class='number'>1</span>,<span class='number'>2</span>,<span class='number'>3</span>)</code> 會 return <code class='undefined'>3</code> (這組 argument 裡面最大的).</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>試看看 <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a> 上的 <code class='ruby'><span class='identifier'><span class='keymethods'>max</span></span>()</code> function. 你可以輸入任何整數或小數給 <code class='ruby'><span class='identifier'><span class='keymethods'>max</span></span>()</code>.</p>

          </div>");
  }
  if(current == 14) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>min()</div>
          </div>
          <div class='article__content'>
            <p><code class='ruby'><span class='identifier'><span class='keymethods'>min</span></span>()</code> returns 所有 arguments 裡面最小的.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>把 <code class='undefined'>minimum</code> 設為 <code class='ruby'><span class='identifier'><span class='keymethods'>min</span></span>()</code> function 和任何你想要的 floats and integers.</p>

          </div>");
  }
  if(current == 15) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>abs()</div>
          </div>
          <div class='article__content'>
            <p><code class='perl'><span class='keyword'>abs</span>()</code> function returns 它 argument 的 <strong>absolute value (絕對值)</strong> , 也就是這個數字距離 <code class='undefined'>0</code> 的距離. 舉例來說, <code class='undefined'>3</code> 和 <code class='diff'><span class='deletion'>-3</span></code> 的絕對值是一樣的: <code class='undefined'>3</code>. <code class='perl'><span class='keyword'>abs</span>()</code> function 一定是 returns positive value (正數), 而且不像 <code class='ruby'><span class='identifier'><span class='keymethods'>max</span></span>()</code> 和 <code class='ruby'><span class='identifier'><span class='keymethods'>min</span></span>()</code>, abs 只接受一個 argument.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在 <a href='javascript:void(0)' class='line-no' data-from='2' data-to=''>line 2</a> 把 <code class='undefined'>absolute</code> 變數指定為一個相等於 <code class='diff'><span class='deletion'>-42</span></code>的absolute value 的 value.</p>

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

                    <p>We are so good at puns.</p>

                  </div>
                </div>
              </div>
          </div>
");
  }
  if(current == 16) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>type()</div>
          </div>
          <div class='article__content'>
            <p>最後, <code class='ruby'><span class='identifier'><span class='keymethods'>type</span></span>()</code> function returns 它收到 argument 的 <strong>type (資料類型)</strong> 如果你在 Python 執行:</p>

<pre><code class='python'><span class='keyword'>print</span> type(<span class='number'>42</span>)
<span class='keyword'>print</span> type(<span class='number'>4.2</span>)
<span class='keyword'>print</span> type(<span class='string'>'spam'</span>)
</code></pre>

<p>Python 會輸出:</p>

<pre><code class='python'>&lt;type <span class='string'>'int'</span>&gt;
&lt;type <span class='string'>'float'</span>&gt;
&lt;type <span class='string'>'str'</span>&gt;
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>讓 Python 在 editor print 出一個 <code class='java'><span class='keyword'>int</span></code>, 一個 <code class='java'><span class='keyword'>float</span></code>, 和一個 <code class='undefined'>str</code> 的 type. 你可以自己決定 <code class='ruby'><span class='identifier'><span class='keymethods'>type</span></span>()</code> 要使用的 values.</p>

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

                    <p>Here's a freebie if you're a bit stuck: <code class='ruby'><span class='identifier'><span class='keymethods'>print</span></span> <span class='identifier'><span class='keymethods'>type</span></span>(<span class='string'>'I have to push the pram a lot'</span>)</code> will cover your <code class='undefined'>str</code> string requirement.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 17) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Review: Functions</div>
          </div>
          <div class='article__content'>
            <p>現在讓我們 review functions.</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>speak</span><span class='params'>(message)</span>:</span>
    <span class='keyword'>return</span> message

<span class='keyword'>if</span> happy():
    speak(<span class='string'>'I'm happy!'</span>)
<span class='keyword'>elif</span> sad():
    speak(<span class='string'>'I'm sad.'</span>)
<span class='keyword'>else</span>:
    speak(<span class='string'>'I don't know what I'm feeling.'</span>)
</code></pre>

<p>上面的程式碼只是給你做為參考!</p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>首先, <code class='python'><span class='keyword'>def</span></code> 一個 function, <code class='undefined'>shut_down</code>, 它可以接受一個 argument 叫做 <code class='perl'><span class='keyword'>s</span></code>. 不要忘記 parentheses 或是 colon!</li>
<li>然後, <code class='java'><span class='keyword'>if</span></code> the <code class='undefined'>shut_down</code> function 收到的 argument <code class='perl'><span class='keyword'>s</span></code> equal to <code class='undefined'>'yes'</code>, 它應該要 <code class='java'><span class='keyword'>return</span> <span class='string'>'Shutting down'</span></code></li>
<li>如果<code class='python'><span class='keyword'>elif</span> s</code> is equal to <code class='undefined'>'no'</code>, 這個 function 英哀要 <code class='java'><span class='keyword'>return</span> <span class='string'>'Shutdown aborted'</span></code>.</li>
<li>最後, 如果 <code class='undefined'>shut_down</code> 收到任何其他的 inputs, the function 應該要 <code class='java'><span class='keyword'>return</span> <span class='string'>'Sorry'</span></code></li>
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

                    <p>Ensure your function outputs appear exactly as shown!</p>

<p>Also, ensure your function <code class='java'><span class='keyword'>return</span></code>s the above values rather than <code class='python'><span class='keyword'>print</span></code>ing them.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 18) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Review: Modules</div>
          </div>
          <div class='article__content'>
            <p>做的好! 現在看看你是不是還記得 import modules (還有 <code class='undefined'>math</code> module 裡有什麼東西).</p>

          </div>
        </div>");
    $(instructions).replaceWith("
<div class='article__inner'>
            <p>用任何你想的方法 import <code class='undefined'>math</code> module. 用 <code class='undefined'>13689</code> call <code class='perl'><span class='keyword'>sqrt</span></code> function  並且把結果 <code class='python'><span class='keyword'>print</span></code> 在 console 上.</p>

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

                    <p>There are three ways you can import the <code class='perl'><span class='keyword'>sqrt</span>()</code> function, but we'd probably go with</p>

<pre><code class='python'><span class='keyword'>from</span> math <span class='keyword'>import</span> sqrt
</code></pre>

<p>You can figure out the rest. We believe in you!</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 19) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Review: Built-In Functions</div>
          </div>
          <div class='article__content'>
            <p>完美! 但是還沒結束, 接下來看前面學的 Python 的 built-in (內建) functions.</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>is_numeric</span><span class='params'>(num)</span>:</span>
    <span class='keyword'>return</span> type(num) == int <span class='keyword'>or</span> type(num) == float:

max(<span class='number'>2</span>, <span class='number'>3</span>, <span class='number'>4</span>) <span class='comment'># 4</span>
min(<span class='number'>2</span>, <span class='number'>3</span>, <span class='number'>4</span>) <span class='comment'># 2</span>

abs(<span class='number'>2</span>) <span class='comment'># 2</span>
abs(-<span class='number'>2</span>) <span class='comment'># 2</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>首先, <code class='python'><span class='keyword'>def</span></code> 一個需要一個 argument 的 function 叫做 <code class='undefined'>distance_from_zero</code>, argument 的名稱你可以自己決定.</li>
<li>如果 argument 的 <code class='ruby'><span class='identifier'><span class='keymethods'>type</span></span></code>  是 <code class='java'><span class='keyword'>int</span></code> 或是 <code class='java'><span class='keyword'>float</span></code>, 這個 function 應該要 <code class='java'><span class='keyword'>return</span></code> argument 的 <code class='perl'><span class='keyword'>abs</span></code>olute value.</li>
<li>否則, 這個 function 應該要 <code class='java'><span class='keyword'>return</span> <span class='string'>'Nope'</span></code></li>
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

                    <p>You can check to see if a value is of <code class='java'>type <span class='keyword'>int</span></code> just as shown in the instructions:</p>

<pre><code class='python'><span class='keyword'>if</span> type(thing) == int <span class='keyword'>or</span> type(thing) == float:
    <span class='comment'># do something with the number</span>
</code></pre>

<p>Make sure your capitalization and punctuation are exactly as shown!</p>

                  </div>
                </div>
              </div>
          </div>");
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


