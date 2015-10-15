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
            <div class='lesson-checkpoint__name'>List accessing</div>
          </div>
          <div class='article__content'>
            <p>這個練習是要取得 list 裡面的資訊!</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>請寫一段指令, print list 裡面的第二個物件.</p>

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

                    <p>Remember that elements in a list start from index 0 and they are accessed in the form</p>

<pre><code class='python'>x[n]
</code></pre>

<p>where <code class='perl'><span class='keyword'>x</span></code> is the name of the list and <code class='undefined'>n</code> is the index in that list that you're trying to access.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 2) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>List element modification</div>
          </div>
          <div class='article__content'>
            <p>我們已經學過如何修改 list 裡面的物件了, 現在再練習一次!</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a>, 把 <code class='undefined'>n</code> list 的第二個物件乘以 5</li>
<li>把原先的第二個物件的 value 改成剛剛的結果.</li>
</ol>

<p>最後再重新 print 一次整個 list!</p>

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

                    <p>An item in a list in Python can be set to a value using the form</p>

<pre><code class='python'>x[n] = v
</code></pre>

<p>where <code class='perl'><span class='keyword'>x</span></code> is the name of the list, <code class='undefined'>n</code> is the index in the array and <code class='undefined'>v</code> is the value you want to set.</p>

                  </div>
                </div>
              </div>
          </div>");    
  }
  if(current == 3) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Appending to a list</div>
          </div>
          <div class='article__content'>
            <p>重新練習一次如何 <code class='undefined'>.append()</code> 物件到 list 的最後面.</p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>把數字 4 加到 list <code class='undefined'>n</code> 的最後面.</p>

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

                    <p>The function to append to the end of a list is</p>

<pre><code class='python'>x.append(item)
</code></pre>

<p>where <code class='perl'><span class='keyword'>x</span></code> is the name of the list and <code class='undefined'>item</code> is the object you want to append.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 4) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Removing elements from lists</div>
          </div>
          <div class='article__content'>
            <p>練習如何 remove list 裡的物件. 有幾個方法可以做這件事.</p>

<ol>
<li><code class='perl'>n.<span class='keyword'>pop</span>(<span class='keyword'>index</span>)</code> 會 remove 在 <code class='perl'><span class='keyword'>index</span></code> 位置的物件, 並 return 這個value:</li>
</ol>

<pre><code class='python'>n = [<span class='number'>1</span>, <span class='number'>3</span>, <span class='number'>5</span>]
n.pop(<span class='number'>1</span>)
<span class='comment'># Returns 3 (the item at index 1)</span>
<span class='keyword'>print</span> n
<span class='comment'># prints [1, 5]</span>
</code></pre>

<ol>
<li><code class='undefined'>n.remove(item)</code>, 如果 <code class='undefined'>item</code> 存在於 list 之中, 移除這個物件:</li>
</ol>

<pre><code class='python'>n.remove(<span class='number'>1</span>)
<span class='comment'># Removes 1 from the list,</span>
<span class='comment'># NOT the item at index 1</span>
<span class='keyword'>print</span> n
<span class='comment'># prints [3, 5]</span>
</code></pre>

<ol>
<li><code class='python'><span class='keyword'>del</span>(n[<span class='number'>1</span>])</code> 就像 <code class='perl'>.<span class='keyword'>pop</span></code> 只是 del 不會reutrn 你移除物件的 value:</li>
</ol>

<pre><code class='python'><span class='keyword'>del</span>(n[<span class='number'>1</span>])
<span class='comment'># Doesn't return anything</span>
<span class='keyword'>print</span> n
<span class='comment'># prints [1, 5]</span>
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>從 list <code class='undefined'>n</code> 中移除第一個物件,用 <code class='perl'>.<span class='keyword'>pop</span>()</code>, <code class='undefined'>.remove()</code>, 或是 <code class='python'><span class='keyword'>del</span></code> 都可以.</p>

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

                    <p>One way of doing this would be</p>

<pre><code class='python'>n.pop(<span class='number'>0</span>)
</code></pre>

<p>where <code class='perl'><span class='keyword'>x</span></code> is the list and <code class='perl'><span class='keyword'>index</span></code> is the item you want to pop off the list. If no index is given, it removes the last item from the list.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 5) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Changing the functionality of a function</div>
          </div>
          <div class='article__content'>
            <p>在這裡要對 function 做一些小修改.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>修改這個 function, 讓她 return 的 value 是 argument 乘以 3.</p>

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

                    <p>You'll want to change the <code class='diff'><span class='addition'>+</span></code> to a <code class='undefined'>*</code>.</p>

                  </div>
                </div>
              </div>
          </div>
");
  }
  if(current == 6) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>More than one argument</div>
          </div>
          <div class='article__content'>
            <p>這個練習是如何在 function 中使用多個 argument.</p>

          </div>
        </div>
");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>Define 一個 function 叫做 <code class='undefined'>add_function</code> , 他要有兩個 parameters: <code class='perl'><span class='keyword'>x</span></code> 和 <code class='perl'><span class='keyword'>y</span></code> 並把它們兩個加在一起.</p>

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

                    <p>A function is defined as follows:</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>my_function</span><span class='params'>(argument1, argument2, etc.)</span>:</span>
    <span class='comment'># Function body goes here</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 7) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Strings in functions</div>
          </div>
          <div class='article__content'>
            <p>複習在 function 中使用 string.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>寫一個 function 叫做 <code class='undefined'>string_function</code>, 他要用一個 string argument: (<code class='perl'><span class='keyword'>s</span></code>) 並且 <code class='java'><span class='keyword'>return</span></code>s 這個 argument 和 <code class='undefined'>'world'</code> 這個 string 加在一起. <code class='undefined'>world</code>  前面不要加空格!</p>

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

                    <p>String concatenation utilizes the <code class='diff'><span class='addition'>+</span></code> symbol:</p>

<pre><code class='python'><span class='keyword'>print</span> <span class='string'>'Hello'</span> + <span class='string'>'world'</span>
<span class='comment'># prints 'Helloworld'</span>
</code></pre>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 8) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Passing a list to a function</div>
          </div>
          <div class='article__content'>
            <p>把 list pass (傳入)一個 function 就和傳入其他類型的 argument 一樣.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>Click Save &amp; Submit Code to see that using a list as an argument in a function is essentially the same as using just a number or string!</p>

          </div>");
  }
  if(current == 9) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Using an element from a list in a function</div>
          </div>
          <div class='article__content'>
            <p>把一個 list pass 到一個 function 就像用 string 或是數字一樣!)</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>first_item</span><span class='params'>(items)</span>:</span>
    <span class='keyword'>print</span> items[<span class='number'>0</span>]

numbers = [<span class='number'>2</span>, <span class='number'>7</span>, <span class='number'>9</span>]
first_item(numbers)
</code></pre>

<ol>
<li>在上面的例子, 我們 define 一個 function 叫做 <code class='undefined'>first_item</code>. 他有一個 argument 叫做 <code class='undefined'>items</code>.</li>
<li>在這個 function 裡面, 我們 <code class='python'><span class='keyword'>print</span></code> <code class='undefined'>items</code> 在 index 0 位置的物件.</li>
<li>在 define function 之後, 我們創造了一個新的 list 叫做 <code class='undefined'>numbers</code>.</li>
<li>最後, 我們 用 <code class='undefined'>numbers</code> 做為 argument, call function: <code class='undefined'>first_item</code>, 他會 prints out <code class='undefined'>2</code>.</li>
</ol>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>修改 <a href='javascript:void(0)' class='line-no' data-from='2' data-to=''>line 2</a>, 讓 <code class='undefined'>list_function</code> 只 returns <code class='perl'><span class='keyword'>x</span></code> index 1 位置的物件 , 而不是整個 <code class='perl'><span class='keyword'>x</span></code> list.</p>

          </div>");
  }
  if(current == 10) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Modifying an element of a list in a function</div>
          </div>
          <div class='article__content'>
            <p>在 Function 裡面修改 list 裡的物件, 就和在 function 外的做法一模一樣.</p>

<pre><code class='python'><span class='function'><span class='keyword'>def</span> <span class='title'>double_first</span><span class='params'>(n)</span>:</span>
    n[<span class='number'>0</span>] = n[<span class='number'>0</span>] * <span class='number'>2</span>

numbers = [<span class='number'>1</span>, <span class='number'>2</span>, <span class='number'>3</span>, <span class='number'>4</span>]
double_first(numbers)
<span class='keyword'>print</span> numbers
</code></pre>

<ol>
<li>創造一個 list 叫做 <code class='undefined'>numbers</code>.</li>
<li>我們用 <code class='undefined'>double_first</code> 這個 function 來修改 numbers list.</li>
<li>最後, print numbers 出來的結果是: <code class='css'><span class='attr_selector'>[2, 2, 3, 4]</span></code></li>
</ol>

<p>當我們把一個 list pass 進一個 function 時, 就像 <code class='undefined'>double_first</code> function 做的, 會變動原先的 list.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>修改 <code class='undefined'>list_function</code> 讓她可以:</p>

<ol>
<li>讓 list 的 index 1 的數字 + 3.</li>
<li>把剛剛的結果 assign 到 list x 的 index 1 的位置.</li>
<li>Return the list. </li>
</ol>

          </div>");
  }
  if(current == 11) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>List manipulation in functions</div>
          </div>
          <div class='article__content'>
            <p>你同樣可以在 function 裡面 append 或是 delete 物件, 就跟在外面一樣.</p>

<pre><code class='python'>my_list = [<span class='number'>1</span>, <span class='number'>2</span>, <span class='number'>3</span>]
my_list.append(<span class='number'>4</span>)
<span class='keyword'>print</span> my_list
<span class='comment'># prints [1, 2, 3, 4]</span>
</code></pre>

<p>上面的例子只是提醒你如何 append 物件到 list.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>Define a function 叫做 <code class='undefined'>list_extender</code>, 它需要一個 parameter 叫做 <code class='undefined'>lst</code>.</li>
<li>在function 裡面, 把數字 9 append 到 <code class='undefined'>lst</code>. </li>
<li>return 這個修改完的 modified list.</li>
</ol>

          </div>");
  }
  if(current == 12) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Printing out a list item by item in a function</div>
          </div>
          <div class='article__content'>
            <p>這個練習是在 function 裡面完成處理 list 所有的相關工作.</p>

<p>先不用擔心 <code class='undefined'>range</code> 這個 function, 我們很快就會解釋.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <ol>
<li>Define a function 叫做 <code class='undefined'>print_list</code>, 他需要一個 argument 叫做 <code class='perl'><span class='keyword'>x</span></code>.</li>
<li>在這function 裡面, print 所有的物件 (以現有的code做為基礎).</li>
<li>Call 這個 function, argument 用 <code class='undefined'>n</code>. </li>
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

                    <p>You can simply place the code on <a href='javascript:void(0)' class='line-no' data-from='3' data-to='4'>lines 3 - 4</a> inside a function definition. Make sure to indent properly! And you'll have to change the <code class='undefined'>n</code> to <code class='perl'><span class='keyword'>x</span></code></p>

                  </div>
                </div>
              </div>
          </div>
");
  }
  if(current == 13) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Modifying each element in a list in a function</div>
          </div>
          <div class='article__content'>
            <p>這個練習旨在說明如何修改 list 裡面的每一個物件. 在 function 裡面這樣做的好處是, 不管你有多少物件都可以一次執行. 就像是 len 這個功能:  <code class='undefined'>len(n)</code> 不管你傳什麼進去, 他都會 reutrn 長度給你.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>創造一個 function 叫做 <code class='undefined'>double_list</code>, 他只需要一個 argument: <code class='perl'><span class='keyword'>x</span></code> (實際使用時會是 list), 他的功能是把 list 裡每一個物件都乘以 2 並 return 乘完結果的 list. (以現有的code做為基礎).</p>

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

                    <p>You can place the code on <a href='javascript:void(0)' class='line-no' data-from='3' data-to='5'>lines 3 - 5</a> inside a function definition. You will need to change the <code class='css'><span class='tag'>n</span><span class='attr_selector'>[i]</span></code>s in the <code class='java'><span class='keyword'>for</span></code> loop to <code class='perl'><span class='keyword'>x</span>[i]</code>. Make sure to indent properly!</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 14) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Passing a range into a function</div>
          </div>
          <div class='article__content'>
            <p>好了, 現在要解釋 range. <code class='undefined'>range()</code> function 是一個產生 list 的功能.</p>

<pre><code class='python'>range(<span class='number'>6</span>) <span class='comment'># =&gt; [0,1,2,3,4,5]</span>
range(<span class='number'>1</span>,<span class='number'>6</span>) <span class='comment'># =&gt; [1,2,3,4,5]</span>
range(<span class='number'>1</span>,<span class='number'>6</span>,<span class='number'>3</span>) <span class='comment'># =&gt; [1,4]</span>
</code></pre>

<p>The <code class='undefined'>range</code> function 有三種不同版本:</p>

<ol>
<li><strong>range</strong>(<em>stop</em>)</li>
<li><strong>range</strong>(<em>start</em>, <em>stop</em>)</li>
<li><strong>range</strong>(<em>start</em>, <em>stop</em>, <em>step</em>)</li>
</ol>

<p>在所有情況下, <code class='undefined'>range()</code> function returns 一個由數字組成的 list, 從 <em>start</em> 開始,到 <em>stop</em>-1 結束. 每一個物件都會依據 <em>step</em> 增加.</p>

<p>如果省略不輸入的話, <em>start</em> 預設值是 0, <em>step</em> 預設值是 1.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>在 <a href='javascript:void(0)' class='line-no' data-from='6' data-to=''>line 6</a>, 把 <code class='undefined'>____</code> 換成一個產生的 list 的 value 是 [0,1,2] 的 <code class='undefined'>range()</code> that returns a list containing <code class='css'><span class='attr_selector'>[0, 1, 2]</span></code>.</p>

          </div>");
  }
  if(current == 15) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Iterating over a list in a function</div>
          </div>
          <div class='article__content'>
            <p>現在我們已經學過 <code class='undefined'>range</code> 了, 我們現在有兩種方法可以 iterate lists.</p>

<p><strong>Method 1</strong> - <code class='python'><span class='keyword'>for</span> item <span class='keyword'>in</span> list</code>:</p>

<pre><code class='python'><span class='keyword'>for</span> item <span class='keyword'>in</span> list:
    <span class='keyword'>print</span> item
</code></pre>

<p><strong>Method 2</strong> - 藉由 index 來 iterate:</p>

<pre><code class='python'><span class='keyword'>for</span> i <span class='keyword'>in</span> range(len(list)):
    <span class='keyword'>print</span> list[i]
</code></pre>

<p><strong>Method 1</strong> 在把 list 裡所有物件都跑一次的情況下很好用, 但是在過程中你沒棒法修改這個 list. <strong>Method 2</strong> 利用 index 來跑迴圈, 讓你在執行的過程同時也可以修改 list 本身. 現在我們還不需要修改 list 你可以用你喜歡的方式! </p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>創造一個 function, return list 裡所有數字的總和.</p>

<ol>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a>, define 一個 function 叫做 <code class='undefined'>total</code>, 讓她接受一個 argument 叫做 <code class='undefined'>numbers</code>. Numbers 之後使用會是一個 list.</li>
<li>在 function 裡面, 創造一個 variable 叫做 <code class='undefined'>result</code> 並把它設定為 0.</li>
<li>用上述的任一方法來 iterate <code class='undefined'>numbers</code> list.</li>
<li>在每一個數字(迴圈每一次執行), 把數字加到 <code class='undefined'>result</code>.</li>
<li>最後, <code class='java'><span class='keyword'>return</span> result</code>.</li>
</ol>

          </div>");
  }
  if(current == 16) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Using strings in lists in functions</div>
          </div>
          <div class='article__content'>
            <p>接下來是看看用 strings!</p>

<pre><code class='python'><span class='keyword'>for</span> item <span class='keyword'>in</span> list:
    <span class='keyword'>print</span> item

<span class='keyword'>for</span> i <span class='keyword'>in</span> range(len(list)):
    <span class='keyword'>print</span> list[i]
</code></pre>

<p>上面的例子只是用來幫你回想上一堂講的兩種 for loop list 的方法.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>創造一個功能來把string 合併在一起.</p>

<ol>
<li>Define a function 叫做 <code class='undefined'>join_strings</code>, 有一個 argument 叫做 <code class='undefined'>words</code>. words 之後會用 list.</li>
<li>在 function 裡面, 創造一個 variable 叫做 <code class='undefined'>result</code>, 並且把它的 value 設定成 <code class='undefined'>''</code>, 一個空的 string.</li>
<li>Iterate <code class='undefined'>words</code> list, 每次都把 loop 的字合併到 <code class='undefined'>result</code>.</li>
<li>最後, <code class='java'><span class='keyword'>return</span></code> <code class='undefined'>result</code>.</li>
</ol>

<p><strong>Don't</strong> add spaces between the joined strings!</p>

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

                    <p>For example,</p>

<pre><code class='python'>join_strings(<span class='string'>'Hello'</span>, <span class='string'>'there'</span>)
</code></pre>

<p>should <code class='java'><span class='keyword'>return</span></code> 'Hellothere'.</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 17) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Using two lists as two arguments in a function</div>
          </div>
          <div class='article__content'>
            <p>在 function 裡面用好幾個 lists 就跟用好幾個 arguments 是一樣意思!</p>

<pre><code class='python'>a = [<span class='number'>1</span>, <span class='number'>2</span>, <span class='number'>3</span>]
b = [<span class='number'>4</span>, <span class='number'>5</span>, <span class='number'>6</span>]
<span class='keyword'>print</span> a + b
<span class='comment'># prints [1, 2, 3, 4, 5, 6]</span>
</code></pre>

<p>上面這個例子是如何把兩個 list 加在一起的做法.</p>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>創在一個功能來把兩個 list 連接在一起.</p>

<ol>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='4' data-to=''>line 4</a>, define 一個 function 叫做 <code class='undefined'>join_lists</code>, 他會需要兩個 arguments, <code class='perl'><span class='keyword'>x</span></code> 和 <code class='perl'><span class='keyword'>y</span></code>. 之後使用時他們兩個都會是 list.</li>
<li>在這個 function 裡, <code class='java'><span class='keyword'>return</span></code> <code class='perl'><span class='keyword'>x</span></code> 和 <code class='perl'><span class='keyword'>y</span></code> 相加的結果.</li>
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

                    <p>You can just use <code class='diff'><span class='addition'>+</span></code> to concatenate two lists. (You don't want to use <code class='undefined'>append</code>, because this just adds the entire second list as a single object at the end of the first.)</p>

                  </div>
                </div>
              </div>
          </div>");
  }
  if(current == 18) {
    $(content).replaceWith("<div class='article__inner'>
          <div class='article__header'>
            <div class='lesson-checkpoint__name'>Using a list of lists in a function</div>
          </div>
          <div class='article__content'>
            <p>最後這個練習會告訴我們 如何使用多層的 list Finally, 還有如何在 function 中使用它.</p>

<pre><code class='python'>list_of_lists = [[<span class='number'>1</span>,<span class='number'>2</span>,<span class='number'>3</span>], [<span class='number'>4</span>,<span class='number'>5</span>,<span class='number'>6</span>]]

<span class='keyword'>for</span> lst <span class='keyword'>in</span> list_of_lists:
    <span class='keyword'>for</span> item <span class='keyword'>in</span> lst:
        <span class='keyword'>print</span> item
</code></pre>

<ol>
<li>在上面這個例子, 我們先創造一個 list, 裡面有兩個物件, 各是一個由數字組成的 list.</li>
<li>然後我們 iterate 一次外層的 list.</li>
<li>兩個內層的 list: (as <code class='undefined'>lst</code>), 我們 iterate list 裡的 numbers (做為 <code class='undefined'>item</code>) 並且print 出來.</li>
</ol>

<p>最後的結果是這樣:</p>

<pre><code class='undefined'>1
2
3
4
5
6
</code></pre>

          </div>
        </div>");
    $(instructions).replaceWith("<div class='article__inner'>
            <p>創造一個 function 叫做 <code class='ruby'><span class='identifier'><span class='keymethods'>flatten</span></span></code>, 它會接受一個 list 並且把這個list 裡面包含的 list 組合成一個單一的list.</p>

<ol>
<li>在 <a href='javascript:void(0)' class='line-no' data-from='3' data-to=''>line 3</a>, define 一個 function 叫做 <code class='ruby'><span class='identifier'><span class='keymethods'>flatten</span></span></code>,  argument 叫做 <code class='undefined'>lists</code>.</li>
<li>做一個新的, 空的list 叫做 <code class='undefined'>results</code>.</li>
<li>Iterate <code class='undefined'>lists</code>. 迴圈裡的變數叫做 <code class='undefined'>numbers</code>.</li>
<li>Iterate <code class='undefined'>numbers</code>.</li>
<li><code class='undefined'>.append()</code> 每一個數字到 <code class='undefined'>results</code> list.</li>
<li>最後, <code class='java'><span class='keyword'>return</span> results</code>.</li>
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

                    <p>For instance, it should turn</p>

<pre><code class='python'>[[<span class='number'>1</span>, <span class='number'>2</span>, <span class='number'>3</span>], [<span class='number'>4</span>, <span class='number'>5</span>, <span class='number'>6</span>]]
</code></pre>

<p>into</p>

<pre><code class='python'>[<span class='number'>1</span>, <span class='number'>2</span>, <span class='number'>3</span>, <span class='number'>4</span>, <span class='number'>5</span>, <span class='number'>6</span>]
</code></pre>

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


