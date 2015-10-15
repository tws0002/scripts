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
            <div class='lesson-checkpoint__name'>Go With the Flow</div>
          </div>
          <div class='article__content'>
            <p>就像在現實生活, 有時候我們會想要成是馬本身可以自己做決定</p>

<p>我們目前所寫到的 Python 程式一次只能做一件事: 它可以把兩個數字加在一起或是 <code class='python'><span class='keyword'>print</span></code> 東西在螢幕上, 但是它們不能選擇要輸出什麼結果.</p>

<p><strong>Control flow</strong> 讓程式可以根據如果發生什麼事, 來選擇產出不同的結果.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>看 editor裡的程式碼. 你可以看到當你熟悉 control flow 後可以寫出的程式. Click Save &amp; Submit to see what happens!</p>

          </div>
");
  }
  if(current == 2) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>比較!</div>
          </div>
          <div class='article__content'>
            <p>讓我們從 control flow 中最簡單的開始: <strong>comparators (比較符號)</strong>. 總共有六種:</p>

<ol>
<li>Equal to (等於) (<code class='undefined'>==</code>)</li>
<li>Not equal to (不等於)(<code class='diff'><span class='change'>!=</span></code>)</li>
<li>Less than (小於)(<code class='undefined'>&lt;</code>)</li>
<li>Less than or equal to (小於或等於)(<code class='undefined'>&lt;=</code>)</li>
<li>Greater than (大於)(<code class='undefined'>&gt;</code>)</li>
<li>Greater than or equal to (大於或等於)(<code class='undefined'>&gt;=</code>)</li>
</ol>

<p>Comparators 會去確認  value 是或不是is equal to, greater than (or equal to), or less than (or equal to) 另一個值.</p>

<p>特別注意: <code class='undefined'>==</code> 比較兩樣東西是否完全相同, 而 <code class='undefined'>=</code> 則是把 value 指定給 variable.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>把每一個 variable 指定為 <code class='python'><span class='built_in'>True</span></code> 或是 <code class='python'><span class='built_in'>False</span></code> 根據你自己的判斷. For Examples (舉例來說), <code class='undefined'>1 &lt; 2</code> 是 <code class='python'><span class='built_in'>True</span></code>, 因為一小於二.</p>

<ol>
<li>Set <code class='undefined'>bool_one</code> 等於 <code class='undefined'>17 &lt; 328</code> 的結果</li>
<li>Set <code class='undefined'>bool_two</code> 等於 <code class='ini'><span class='setting'>100 =<span class='value'>= (<span class='number'>2</span>&nbsp;*&nbsp;<span class='number'>50</span>)</span></span></code></li>
<li>Set <code class='undefined'>bool_three</code> 等於 <code class='undefined'>19 &lt;= 19</code> 的結果

<ol>
<li>Set <code class='undefined'>bool_four</code> 等於 <code class='diff'><span class='deletion'>-22 &gt;= -18</span></code> 的結果</li>
<li>Set <code class='undefined'>bool_five</code> 等於 <code class='undefined'>99 != (98&nbsp;+&nbsp;1)</code> 的結果</li>
</ol></li>
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

                    <p>Remember, you set variables like this:</p>

<pre><code class='python'>bool_one = <span class='built_in'>True</span>
</code></pre>

<p>記住，檢查等不等於是用兩個等號:</p>

<pre><code class='python'><span class='built_in'>True</span> == <span class='built_in'>True</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");    
  }
  if(current == 3) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>比較!</div>
          </div>
          <div class='article__content'>
            <p>你已經理解 expressions 和 comparators 了.</p>

<p>但 <em>extreme(極端的)</em> expressions and comparators 又如何呢?</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>讓我們用比較複雜的 expressions 來執行一次 comparators. 一樣根據你自己的判斷把每一個 variable 設定為 <code class='python'><span class='built_in'>True</span></code> 或是 <code class='python'><span class='built_in'>False</span></code> .</p>

<ol>
<li>把 variable <code class='undefined'>bool_one</code> 的結果設定為 <code class='undefined'>(20&nbsp;-&nbsp;10)&nbsp;&gt;&nbsp;15</code></li>
<li>把 variable <code class='undefined'>bool_two</code> 的結果設定為 <code class='perl'>(<span class='number'>10</span>&nbsp;+&nbsp;<span class='number'>17</span>)&nbsp;==&nbsp;<span class='number'>3</span><span class='variable'>**</span><span class='number'>16</span></code></li>
<li>把 variable <code class='undefined'>bool_three</code> 的結果設定為 <code class='perl'><span class='number'>1</span><span class='variable'>**</span><span class='number'>2</span>&nbsp;&lt;=&nbsp;<span class='number'>-1</span></code></li>
<li>把 variable <code class='undefined'>bool_four</code> 的結果設定為 <code class='undefined'>40&nbsp;*&nbsp;4 &gt;=&nbsp;-4</code></li>
<li>把 variable <code class='undefined'>bool_five</code> 的結果設定為 <code class='perl'><span class='number'>100</span> != <span class='number'>10</span><span class='variable'>**</span><span class='number'>2</span></code></li>
</ol>

          </div>");
  }
  if(current == 4) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>交換一下</div>
          </div>
          <div class='article__content'>
            <p>比較的結果只有 True 或是 False, 也就是之前學的 booleans <a href='http://www.codecademy.com/courses/introduction-to-python-6WeG3/0/3'>this exercise</a>.</p>

<pre><code class='python'><span class='comment'># Make me true!</span>
bool_one = <span class='number'>3</span> &lt; <span class='number'>5</span>
</code></pre>

<p>讓我們交換一下, 你來寫 expression, 而我們會給你結果: True or False, 就像上面的例子那樣.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>Editor 裡面會指定 boolean value, 寫一個會產生這個結果的 expression.</p>

<p>記住, comparators 有: <code class='undefined'>==</code>, <code class='diff'><span class='change'>!=</span></code>, <code class='undefined'>&gt;</code>, <code class='undefined'>&gt;=</code>, <code class='undefined'>&lt;</code>, and <code class='undefined'>&lt;=</code>.</p>

<p>至少要使用三種!</p>

<p>不要直接用 <code class='python'><span class='built_in'>True</span></code> and <code class='python'><span class='built_in'>False</span></code>! That's cheating!</p>

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

                    <p>For <code class='undefined'>bool_two</code>, you might try:</p>

<pre><code class='python'>bool_one = <span class='number'>8</span> &gt; <span class='number'>7</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 5) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>To Be and/or Not to Be</div>
          </div>
          <div class='article__content'>
            <p><strong>Boolean operators</strong> 用結果正確或不正確來比較 statements 和 result in . 共有三種 boolean operators:</p>

<ol>
<li><code class='python'><span class='keyword'>and</span></code>, 確認是否兩個 statements 都是 <code class='python'><span class='built_in'>True</span></code>;</li>
<li><code class='python'><span class='keyword'>or</span></code>, 確認是否至少有一個 statements 是 <code class='python'><span class='built_in'>True</span></code>;</li>
<li><code class='python'><span class='keyword'>not</span></code>, 確認 statement 為否 (False).</li>
</ol>

<p>接下來會一個一個 operator 講.</p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>看一下 editor裡的表格, 如果看不懂就算了!</p>

<p>Click Save &amp; Submit to continue.</p>

          </div>");
  }
  if(current == 6) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>And</div>
          </div>
          <div class='article__content'>
            <p>The boolean operator <code class='python'><span class='keyword'>and</span></code> 會 returns <code class='python'><span class='built_in'>True</span></code> 當 and 兩邊的結果都為真 <code class='python'><span class='keyword'>and</span></code> . 例:</p>

<ul>
<li><code class='python'><span class='number'>1</span> &lt; <span class='number'>2</span> <span class='keyword'>and</span> <span class='number'>2</span> &lt; <span class='number'>3</span></code> is <code class='python'><span class='built_in'>True</span></code>;</li>
<li><code class='xml'>1 <span class='tag'>&lt; <span class='attribute'>2</span> <span class='attribute'>and</span> <span class='attribute'>2</span> &gt;</span> 3</code> is <code class='python'><span class='built_in'>False</span></code>.</li>
</ul>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>接下來做 <code class='python'><span class='keyword'>and</span></code> 的練習. 根據下面的 boolean value 輸入正確的 variables.</p>

<ol>
<li>Set <code class='undefined'>bool_one</code> 等於結果: <code class='python'><span class='built_in'>False</span> <span class='keyword'>and</span> <span class='built_in'>False</span></code></li>
<li>Set <code class='undefined'>bool_two</code> 等於結果: <code class='perl'>-(-(-(<span class='number'>-2</span>))) == <span class='number'>-2</span> <span class='keyword'>and</span> <span class='number'>4</span> &gt;= <span class='number'>16</span><span class='variable'>**</span><span class='number'>0</span>.<span class='number'>5</span></code></li>
<li>Set <code class='undefined'>bool_three</code> 等於結果: <code class='python'><span class='number'>19</span> % <span class='number'>4</span> != <span class='number'>300</span> / <span class='number'>10</span> / <span class='number'>10</span> <span class='keyword'>and</span> <span class='built_in'>False</span></code></li>
<li>Set <code class='undefined'>bool_four</code> 等於結果: <code class='perl'>-(<span class='number'>1</span><span class='variable'>**</span><span class='number'>2</span>) &lt; <span class='number'>2</span><span class='variable'>**</span><span class='number'>0</span> <span class='keyword'>and</span> <span class='number'>10</span> % <span class='number'>10</span> &lt;= <span class='number'>20</span> - <span class='number'>10</span> * <span class='number'>2</span></code></li>
<li>Set <code class='undefined'>bool_five</code> 等於結果: <code class='python'><span class='built_in'>True</span> <span class='keyword'>and</span> <span class='built_in'>True</span></code></li>
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

                    <p>Remember that a number raised to the 1/2 power is equal to the square root of that number! (For example, <code class='perl'><span class='number'>25</span><span class='variable'>**</span><span class='number'>0</span>.<span class='number'>5</span></code> is equal to the square root of <code class='undefined'>25</code>, which is <code class='undefined'>5</code>.)</p>

<p>Be careful with <code class='undefined'>bool_four</code>—there's a big difference between <code class='perl'><span class='number'>-1</span><span class='variable'>**</span><span class='number'>2</span></code> and <code class='perl'>(<span class='number'>-1</span>)<span class='variable'>**</span><span class='number'>2</span></code>! This is meant to be tricky. Test it out in the <a href='http://labs.codecademy.com/'>labs</a> if you're unsure.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 7) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Or</div>
          </div>
          <div class='article__content'>
            <p>The boolean operator <code class='python'><span class='keyword'>or</span></code> returns <code class='python'><span class='built_in'>True</span></code> 當至少有<code class='python'><span class='keyword'>or</span></code>一邊的 expression 結果為 true. 例:</p>

<ul>
<li><code class='xml'>1 <span class='tag'>&lt; <span class='attribute'>2</span> <span class='attribute'>or</span> <span class='attribute'>2</span> &gt;</span> 3</code> is <code class='python'><span class='built_in'>True</span></code>;</li>
<li><code class='python'><span class='number'>1</span> &gt; <span class='number'>2</span> <span class='keyword'>or</span> <span class='number'>2</span> &gt; <span class='number'>3</span></code> is <code class='python'><span class='built_in'>False</span></code>.</li>
</ul>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>練習時間!</p>

<ol>
<li>Set <code class='undefined'>bool_one</code> 等於結果: <code class='perl'><span class='number'>2</span><span class='variable'>**</span><span class='number'>3</span> == <span class='number'>108</span> % <span class='number'>100</span> <span class='keyword'>or</span> <span class='string'>'Cleese'</span> == <span class='string'>'King Arthur'</span></code></li>
<li>Set <code class='undefined'>bool_two</code> 等於結果: <code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>False</span></code></li>
<li>Set <code class='undefined'>bool_three</code> 等於結果: <code class='python'><span class='number'>100</span>**<span class='number'>0.5</span> &gt;= <span class='number'>50</span> <span class='keyword'>or</span> <span class='built_in'>False</span></code></li>
<li>Set <code class='undefined'>bool_four</code> 等於結果: <code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>True</span></code></li>
<li>Set <code class='undefined'>bool_five</code> 等於結果: <code class='perl'><span class='number'>1</span><span class='variable'>**</span><span class='number'>100</span> == <span class='number'>100</span><span class='variable'>**</span><span class='number'>1</span> <span class='keyword'>or</span> <span class='number'>3</span> * <span class='number'>2</span> * <span class='number'>1</span> != <span class='number'>3</span> + <span class='number'>2</span> + <span class='number'>1</span></code></li>
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

                    <p>Remember, <code class='python'><span class='keyword'>or</span></code> is <code class='python'><span class='built_in'>True</span></code> when either (or both!) of the expressions involved are true.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 8) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Not</div>
          </div>
          <div class='article__content'>
            <p>The boolean operator <code class='python'><span class='keyword'>not</span></code>, 當結果為否時, 會 return <code class='python'><span class='built_in'>True</span></code> , 當結果為真時, 會 return <code class='python'><span class='built_in'>False</span></code>.</p>

<p>例:</p>

<ul>
<li><code class='python'><span class='keyword'>not</span> <span class='built_in'>False</span></code> 結果是 <code class='python'><span class='built_in'>True</span></code>, while <code class='python'><span class='keyword'>not</span> <span class='number'>41</span> &gt; <span class='number'>40</span></code> 結果是 <code class='python'><span class='built_in'>False</span></code>.</li>
</ul>

          </div>
        </div>");
    $(instructions).replaceWith("
<div class='article__inner'>
            <p>Let's get some practice with <code class='python'><span class='keyword'>not</span></code>.</p>

<ol>
<li>Set <code class='undefined'>bool_one</code> equal to the result of <code class='python'><span class='keyword'>not</span> <span class='built_in'>True</span></code></li>
<li>Set <code class='undefined'>bool_two</code> equal to the result of <code class='perl'><span class='keyword'>not</span> <span class='number'>3</span><span class='variable'>**</span><span class='number'>4</span> &lt; <span class='number'>4</span><span class='variable'>**</span><span class='number'>3</span></code></li>
<li>Set <code class='undefined'>bool_three</code> equal to the result of <code class='python'><span class='keyword'>not</span> <span class='number'>10</span> % <span class='number'>3</span> &lt;= <span class='number'>10</span> % <span class='number'>2</span></code></li>
<li>Set <code class='undefined'>bool_four</code> equal to the result of <code class='perl'><span class='keyword'>not</span> <span class='number'>3</span><span class='variable'>**</span><span class='number'>2</span> + <span class='number'>4</span><span class='variable'>**</span><span class='number'>2</span> != <span class='number'>5</span><span class='variable'>**</span><span class='number'>2</span></code></li>
<li>Set <code class='undefined'>bool_five</code> equal to the result of <code class='python'><span class='keyword'>not</span> <span class='keyword'>not</span> <span class='built_in'>False</span></code></li>
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

                    <p>Remember, <code class='python'><span class='keyword'>not</span> <span class='built_in'>True</span></code> is <code class='python'><span class='built_in'>False</span></code> and <code class='python'><span class='keyword'>not</span> <span class='built_in'>False</span></code> is <code class='python'><span class='built_in'>True</span></code>. So, for example, <code class='undefined'>bool_one</code> should be:</p>

<pre><code class='python'>bool_one = <span class='built_in'>False</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 9) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>This and That (or This, But Not That!)</div>
          </div>
          <div class='article__content'>
            <p>Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:</p>

<ol>
<li><code class='python'><span class='keyword'>not</span></code> is evaluated first;</li>
<li><code class='python'><span class='keyword'>and</span></code> is evaluated next;</li>
<li><code class='python'><span class='keyword'>or</span></code> is evaluated last.</li>
</ol>

<p>For example, <code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='keyword'>not</span> <span class='built_in'>False</span> <span class='keyword'>and</span> <span class='built_in'>False</span></code> returns <code class='python'><span class='built_in'>True</span></code>. If this isn't clear, look at the Hint.</p>

<p>Parentheses <code class='undefined'>()</code> ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>Assign <code class='python'><span class='built_in'>True</span></code> or <code class='python'><span class='built_in'>False</span></code> as appropriate for <code class='undefined'>bool_one</code> through <code class='undefined'>bool_five</code>.</p>

<ol>
<li>Set <code class='undefined'>bool_one</code> equal to the result of <code class='python'><span class='built_in'>False</span> <span class='keyword'>or</span> <span class='keyword'>not</span> <span class='built_in'>True</span> <span class='keyword'>and</span> <span class='built_in'>True</span></code></li>
<li>Set <code class='undefined'>bool_two</code> equal to the result of <code class='python'><span class='built_in'>False</span> <span class='keyword'>and</span> <span class='keyword'>not</span> <span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>True</span></code></li>
<li>Set <code class='undefined'>bool_three</code> equal to the result of <code class='python'><span class='built_in'>True</span> <span class='keyword'>and</span> <span class='keyword'>not</span> (<span class='built_in'>False</span> <span class='keyword'>or</span> <span class='built_in'>False</span>)</code></li>
<li>Set <code class='undefined'>bool_four</code> equal to the result of <code class='python'><span class='keyword'>not</span> <span class='keyword'>not</span> <span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>False</span> <span class='keyword'>and</span> <span class='keyword'>not</span> <span class='built_in'>True</span></code></li>
<li>Set <code class='undefined'>bool_five</code> equal to the result of <code class='python'><span class='built_in'>False</span> <span class='keyword'>or</span> <span class='keyword'>not</span> (<span class='built_in'>True</span> <span class='keyword'>and</span> <span class='built_in'>True</span>)</code></li>
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

                    <ol>
<li><code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='keyword'>not</span> <span class='built_in'>False</span> <span class='keyword'>and</span> <span class='built_in'>False</span></code>. <code class='python'><span class='keyword'>not</span></code> gets evaluated first, so we have</li>
<li><code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>True</span> <span class='keyword'>and</span> <span class='built_in'>False</span></code>. <code class='python'><span class='keyword'>and</span></code> goes next, so we get</li>
<li><code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>False</span></code>. As we've seen, <code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>False</span></code> is <code class='python'><span class='built_in'>True</span></code>, so the value finally returned is <code class='python'><span class='built_in'>True</span></code>!</li>
</ol>

                  </div>
                </div>
              </div>
          </div>
");
  }
  if(current == 10) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Mix 'n' Match</div>
          </div>
          <div class='article__content'>
            <p>Great work! We're almost done with boolean operators.</p>

<pre><code class='python'><span class='comment'># Make me false</span>
bool_one = (<span class='number'>2</span> &lt;= <span class='number'>2</span>) <span class='keyword'>and</span> <span class='string'>'Alpha'</span> == <span class='string'>'Bravo'</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Mix 'n' Match</div>
          </div>
          <div class='article__content'>
            <p>Great work! We're almost done with boolean operators.</p>

<pre><code class='python'><span class='comment'># Make me false</span>
bool_one = (<span class='number'>2</span> &lt;= <span class='number'>2</span>) <span class='keyword'>and</span> <span class='string'>'Alpha'</span> == <span class='string'>'Bravo'</span>
</code></pre>

          </div>
        </div>");
  }
  if(current == 11) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Conditional Statement Syntax </div>
          </div>
          <div class='article__content'>
            <p><code class='java'><span class='keyword'>if</span></code> 是 conditional statement (條件式的判斷), 當判斷為 <code class='python'><span class='built_in'>True</span></code> 後會執行特定的程式碼.</p>

<p><code class='java'><span class='keyword'>if</span></code> 語法範例:</p>

<pre><code class='python'><span class='keyword'>if</span> <span class='number'>8</span> &lt; <span class='number'>9</span>:
    <span class='keyword'>print</span> <span class='string'>'Eight is less than nine!'</span>
</code></pre>

<p>在這個例子裡, <code class='undefined'>8 &lt; 9</code> 是用來判斷的 expression,  <code class='python'><span class='keyword'>print</span> <span class='string'>'Eight is less than nine!'</span></code> 則是判斷後要執行的程式碼.</p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>如果你認為 <code class='python'><span class='keyword'>print</span></code> statement 在執行後會顯示在 console 上, 把 <code class='undefined'>response</code> 設為 <code class='cpp'><span class='string'>'Y'</span></code>; 不然則設定為 <code class='cpp'><span class='string'>'N'</span></code>.</p>

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

                    <p>Make sure to set <code class='undefined'>response</code> to <code class='undefined'>'Y'</code> or <code class='undefined'>'N'</code>!</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 12) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>If You're Having...</div>
          </div>
          <div class='article__content'>
            <p>現在來做一些 <code class='java'><span class='keyword'>if</span></code> statements 的練習. 記得語法像下面這樣:</p>

<pre><code class='python'><span class='keyword'>if</span> some_function():
    <span class='comment'># block line one</span>
    <span class='comment'># block line two</span>
    <span class='comment'># et cetera</span>
</code></pre>

<p>看上面的例子, 當 <code class='undefined'>some_function()</code> returns <code class='python'><span class='built_in'>True</span></code>, 下面 indented block 裡的程式碼會被執行. 相反的要是 <code class='undefined'>some_function()</code> returns <code class='python'><span class='built_in'>False</span></code> <code class='python'><span class='built_in'>False</span></code>, indented block 裡的程式碼會被略過不執行.</p>

<p>還有, 注意 <code class='java'><span class='keyword'>if</span></code> 之後需要有個冒號.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在 editor 中你會看到兩個 functions. 之後會在做解釋.</p>

<ol>
<li>把 <a href='javascript:void(0)' class='line-no' data-from='2' data-to=''>line 2</a> 的 underline (底線)  換成一個會 returns <code class='python'><span class='built_in'>True</span></code>的 expression.</li>
<li>把 <a href='javascript:void(0)' class='line-no' data-from='6' data-to=''>line 6</a> 的 underline 換成一個會 returns <code class='python'><span class='built_in'>True</span></code> 的 expression.</li>
</ol>

<p>如果你成功的完成練習, 兩個 <code class='css'>'<span class='tag'>Success</span> <span class='id'>#1</span>'</code> and <code class='css'>'<span class='tag'>Success</span> <span class='id'>#2</span>'</code> 會被 print 在 console 裡.</p>

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

                    <p>Here's an example to remind you of the syntax:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>true_function</span><span class='params'>()</span>:</span>
    <span class='keyword'>if</span> <span class='number'>1</span> &lt; <span class='number'>2</span>:
        <span class='keyword'>return</span> <span class='built_in'>True</span>
</code></pre>

<p>Don't forget the colon at the end of the line!</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 13) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Else Problems, I Feel Bad for You, Son...</div>
          </div>
          <div class='article__content'>
            <p>The <code class='java'><span class='keyword'>else</span></code> statement 補足了 <code class='java'><span class='keyword'>if</span></code> statement. 一組 <code class='java'><span class='keyword'>if</span></code>/<code class='java'><span class='keyword'>else</span></code> 的意思是: 當 expression 為真時, 跑接下來的 indented block 的程式碼; 不然執行 else satement 下面 indent block 內的程式碼.</p>

<p>和 <code class='java'><span class='keyword'>if</span></code>, 不同 <code class='java'><span class='keyword'>else</span></code> 不需要依賴 expression 來決定是否執行. 例:</p>

<pre><code class='python'><span class='keyword'>if</span> <span class='number'>8</span> &gt; <span class='number'>9</span>:
    <span class='keyword'>print</span> <span class='string'>'I don't printed!'</span>
<span class='keyword'>else</span>:
    <span class='keyword'>print</span> <span class='string'>'I get printed!'</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>完成 <code class='java'><span class='keyword'>else</span></code> statements 之後的程式碼. 要記得 indentation!</p>

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

                    <p>To complete your <code class='java'><span class='keyword'>else</span></code> statement lines, the <em>only</em> thing you need to do is add <code class='python'><span class='built_in'>False</span></code> after the <code class='java'><span class='keyword'>return</span></code>s on <a href='javascript:void(0)' class='line-no' data-from='8' data-to=''>lines 8</a> and 14.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 14) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>I Got 99 Problems, But a Switch Ain't One</div>
          </div>
          <div class='article__content'>
            <p>'Elif' 是 'else if.' 的簡寫. 意思是指 '否則的話, 接下來的 expression 如果為真,執行接下來的程式碼!'</p>

<pre><code class='python'><span class='keyword'>if</span> <span class='number'>8</span> &gt; <span class='number'>9</span>:
    <span class='keyword'>print</span> <span class='string'>'I don't get printed!'</span>
<span class='keyword'>elif</span> <span class='number'>8</span> &lt; <span class='number'>9</span>:
    <span class='keyword'>print</span> <span class='string'>'I get printed!'</span>
<span class='keyword'>else</span>:
    <span class='keyword'>print</span> <span class='string'>'I also don't get printed!'</span>
</code></pre>

<p>在上面的例子, <code class='python'><span class='keyword'>elif</span></code> statement 只有在一開始的 <code class='java'><span class='keyword'>if</span></code> statement if <code class='python'><span class='built_in'>False</span></code>時, 才會被 check 是否為真.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='2' data-to=''>line 2</a>, 填入 <code class='java'><span class='keyword'>if</span></code> 要確認的 statement <em>if</em> <code class='undefined'>answer</code> is greater than 5.</li>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='4' data-to=''>line 4</a>, 填入 <code class='python'><span class='keyword'>elif</span></code>, 讓這 function 在 <code class='undefined'>answer</code> 小於5的時後會 return <code class='diff'><span class='deletion'>-1</span></code>.</li>
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

                    <p>Make sure the <code class='java'><span class='keyword'>if</span></code> and <code class='python'><span class='keyword'>elif</span></code> statements end with colons <code class='undefined'>:</code></p>

<p>Your code should look something like:</p>

<pre><code class='python'><span class='keyword'>if</span> EXPRESSION:
    do something
<span class='keyword'>elif</span> OTHER EXPRESSION:
    do something
<span class='keyword'>else</span>:
    do something
</code></pre>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 15) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>The Big If</div>
          </div>
          <div class='article__content'>
            <p>你在這堂課學到這些東西:</p>

<p><strong>Comparators</strong></p>

<pre><code class='python'><span class='number'>3</span> &lt; <span class='number'>4</span>
<span class='number'>5</span> &gt;= <span class='number'>5</span>
<span class='number'>10</span> == <span class='number'>10</span>
<span class='number'>12</span> != <span class='number'>13</span>
</code></pre>

<p><strong>Boolean operators</strong></p>

<pre><code class='python'><span class='built_in'>True</span> <span class='keyword'>or</span> <span class='built_in'>False</span> 
(<span class='number'>3</span> &lt; <span class='number'>4</span>) <span class='keyword'>and</span> (<span class='number'>5</span> &gt;= <span class='number'>5</span>)
this() <span class='keyword'>and</span> <span class='keyword'>not</span> that()
</code></pre>

<p><strong>Conditional statements</strong></p>

<pre><code class='python'><span class='keyword'>if</span> this_might_be_true():
    <span class='keyword'>print</span> <span class='string'>'This really is true.'</span>
<span class='keyword'>elif</span> that_might_be_true():
    <span class='keyword'>print</span> <span class='string'>'That is true.'</span>
<span class='keyword'>else</span>:
    <span class='keyword'>print</span> <span class='string'>'None of the above.'</span>
</code></pre>

<p></p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>寫一個 <code class='undefined'>the_flying_circus()</code> 裡的 <code class='java'><span class='keyword'>if</span></code> statement. 它必須包含下面幾樣東西:</p>

<ol>
<li><code class='java'><span class='keyword'>if</span></code>, <code class='python'><span class='keyword'>elif</span></code>, and <code class='java'><span class='keyword'>else</span></code> statements;</li>
<li>至少一個: <code class='python'><span class='keyword'>and</span></code>, <code class='python'><span class='keyword'>or</span></code>, or <code class='python'><span class='keyword'>not</span></code>;</li>
<li>A comparator (<code class='undefined'>==</code>, <code class='diff'><span class='change'>!=</span></code>, <code class='undefined'>&lt;</code>, <code class='undefined'>&lt;=</code>, <code class='undefined'>&gt;</code>, or <code class='undefined'>&gt;=</code>);</li>
<li>最後在執行的時候, <code class='undefined'>the_flying_circus()</code> 必須 <code class='python'><span class='keyword'>return</span> <span class='built_in'>True</span></code> .</li>
</ol>

<p><code class='java'><span class='keyword'>if</span></code> statements 之後要加上 <code class='undefined'>:</code>!</p>

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

                    <p>Be careful with your indentation—<code class='undefined'>the_flying_circus()</code> is a function (which we'll get to in the next unit), and as you can see from the comment, function blocks are indented the same way <code class='java'><span class='keyword'>if</span></code>, <code class='python'><span class='keyword'>elif</span></code>, and <code class='java'><span class='keyword'>else</span></code> blocks are.</p>

<p>Your code should look something like this:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>the_flying_circus</span><span class='params'>()</span>:</span>
    <span class='keyword'>if</span> condition:
        <span class='comment'># Do something!</span>
    <span class='keyword'>elif</span> condition:
        <span class='comment'># Do something else!</span>
    <span class='keyword'>else</span>:
        <span class='comment'># Do yet another thing!</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>
");
  }
  $(".is-hidden-if-is-expanded").replaceWith("<span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>");
  $(".is-shown-if-is-expanded--inline").replaceWith("<span class='is-shown-if-is-expanded--inline'><b>暗示</b></span>");  
  $(".lesson__course-name.one-line-text.js-course-name").text("Python Conditionals and Control Flow(比較和流程控制)");   
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


