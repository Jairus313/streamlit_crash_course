
## Hey There..! I am **[Sudeep Nellur](https://sudeepnellur.tech/)** aka **[Jairus313](https://sudeepnellur.tech/** :sunglasses:. Here I am writing this little crash course about **[Streamlit.io](https://streamlit.io/)** which will be more than enough for you to get started and start rolling some cool apps. So let's wrap our head around.!

  
## About Streamlit..!

Before starting with actually let's answers some basics questions.

Q. What is the Streamlit.io?</br>
A. Streamlit.io is the app framework for machine learning and data science solution where you can write few lines of python code and get your app up running within minutes and you can host too, if you want to share with your friends. More on [Streamlit.io](streamlit.io)</br></br>

Q. Why Streamlit.io or UI in general needed?</br>
A. <img  src="assets/tweet.png"  alt="https://twitter.com/jairus313/status/1472974950508089348?s=20"  width="500"/>

Q. What are the pre-requisites?</br>
A. Streamlit is python framework, So Python is must and enough but if you already know Python GUI like PyQt or TKinter and HTML then it would be really.

With these being clear to you, let's start and feel free to jump around on the topic with which you are interested.

<hr>

## Index

- [Installation and Get started](#Installation)
- [General Synatx](#general_syntax)
- [Markdowns](#markdown)
- [Latex](#latex)
- [Write](#write)
- [Display](#display)
- [Plots](#plot)
- [Media](#media)
- [Widgets](#widgets)
- [Sidebars](#sidebars)
- [Animations](#animations)

<hr>

<a  id="Installation"></a>
### Installation and Get started

Before start installing the streamlit which is super easy to install make sure that you have got python package manager installed properly. If this is checked then open your terminal or cmd and run the below command.

```sh
# for windows.
pip install streamlit

# for linux.
pip3 install streamlit
```

This is will take little while and after successfully installed, You can check your installed by running the below command. And this will take you to home page of streamlit which indicates that everything installed properly.

```sh
streamlit hello
```

**Note:** Streamlit in background uses protobuf as it's internal dependencies, Install Google protobuf before installing streamlit first. For more refer this [link](https://stackoverflow.com/questions/61922334/how-to-solve-attributeerror-module-google-protobuf-descriptor-has-no-attribu) .

Now that you have installed it properly, Create python script and write the below code.

```python
# importing library, will be using it as "st" throughtout the blog.
import streamlit as st

# Just a title, will get on this later.
st.title('Just a title')
```

Save this script then open the terminal and run below the command which will make app to boot up and this will open your browser for it.

```sh
streamlit run your_script_name.py
```
<hr>

<a  id="general_syntax"></a>
### General Syntax

Streamlit is very simple and straight forward App framework, the syntax follows as below.

```python
st.<element_name>(<value>)
```

Here;

 - **st**: Streamlit class instance
 - **element_name**: Widget/Component
 - **value**: Value for that element

Example:
```python
# importing library.
import streamlit as st

# title is the fucntion for title and yes I've just embedded emoji right away.
st.title('Jairus313 - This is my made up name :sunglasses:')
```

As above mentioned code, we will be importing the **streamlit** as **st** for convenience and next we will create title which is h1 tag in html by using calling the function **title**  and that will be taking one required parameter which is text and yes, you can add emoji too.  Here let's us save this code as **script.py** and run the below command to boot up.

```sh
streamlit run script.py
```

And that's it, Your app will be up and running and this syntax will remains same with little modification which makes streamlit a very handy framework to get started. And to stop, just go back to the terminal/cmd and hit ctrl+ c.

<hr>

<a  id="markdown"></a>
### Markdowns

Markdown is which light-weight markup language which will be used to build up some visually appealing  documentation with some simple text. Here markdown is support in streamlit which give more control to developer and for more do refer this [link](https://www.markdownguide.org/getting-started/). Let's have a look on some below.

Syntax:
```sh
st.markdown(" your markdown ")
```

Code Example:
```python
# importing library.
import streamlit as st

# and you have more control, If you use markdown syntax.
st.markdown("""
			# h1 tag
			## h2 tag
			### h3 tag
			#### h4 tag
			##### h5 tag
			###### h6 tag
			""")

## bold text.
st.markdown("Some **Bold** text")

# italic text.
st.markdown("Some _Italic_ text")

# strikethrough text.
st.markdown("Some ~~strikethrough~~ text")
```

<hr>

<a  id="latex"></a>
### Latex

Latex are fun and interesting typesetting system and this will be used most in technical and scientific documentation, to put up everything in simple terms it's all those wizard/greek signs or equations that you see in documentations. For more do refer this [link](https://typeset.io/resources/learn-latex-beginners-step-by-step-guide/)

Syntax:
```sh
#"r" for reading it as text.
st.latex(r''' your greek equation ''')
```

Code Example:
```python
# importing library.
import streamlit as st

# latex
# Do run this code by yourself to see the equation.;)
st.latex(r'''
		x^2 = \frac{n^2+n}{10}
		''')

st.latex(r'''
		a + ar + a r^2 + a r^3 +  \cdots + a r^{n-1} =
		\sum_{k=0}^{n-1} ar^k =
		a \left(\frac{1-r^{n}}{1-r}\right)
		''')
```

<hr>

<a  id="write"></a>
### Write

Streamlit's write is basically a terminal in the app itself and it's most powerful function since it acts as terminal. Here you do many things like printing your output to plotting up the graphs. Let's have a look on it.

Syntax:
```sh
st.write("output")
```

Code Example:
```python
# importing library.
import streamlit as st
import pandas as pd
import numpy as np

# to print anything using write.
st.write(1234)

st.write("# Can be used as markdown too.")

st.write("sum of two values", 2+2)

# can display the arrays too.
data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
columns=['a', 'b', 'c'])

st.write("before the dataframe", data, "after the dataframe")
```

<hr>

<a  id="display"></a>
### Display

As the name suggests Streamlit Display will be all tables, arrays, json and also some cool metrics too.

Syntax:
```sh
# dataframes/array.
st.dataframe("dataframe")

# tables.
st.table("tables")

# json.
st.json({"your":"json"})

# metrics.
st.metric(label="label", value="value", delta="percentage")
```

Code Example:
```python
# importing library.
import streamlit as st
import pandas as pd
import numpy as np

# dataframe.
# values in 2D array with column name.
df = pd.DataFrame(
	np.array([["Sudeep Nellur", "Machine Learning Engineer", "https://sudeepnellur.tech/"]]),
	columns=("Name", "Desgination", "Portfolio"))

st.dataframe(df)

df = pd.DataFrame(
np.random.randn(10, 10),
columns=('col %d' % i for i in range(10)))

st.dataframe(df)

# tables.
# in table everything will be displayed
st.table(df)

# some cool metric.
st.metric(label="Petrol", value="100 ₹", delta="+10%")

# some json too.
st.json({
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
			},
			"topping":
				[
					{ "id": "5001", "type": "None" },
					{ "id": "5002", "type": "Glazed" },
					{ "id": "5005", "type": "Sugar" },
					{ "id": "5007", "type": "Powdered Sugar" },
					{ "id": "5006", "type": "Chocolate with Sprinkles" },
					{ "id": "5003", "type": "Chocolate" },
					{ "id": "5004", "type": "Maple" }
				]
		})
```

<hr>

<a  id="plot"></a>
### Plots

Streamlit plot's as similar as display, Here instead of tables we will display graphs, plot and diagrams too. Some of them are line chart, area chart, bar chart and many more.

Syntax:
```sh
# line chart
st.line_chart("chart_data")

# area chart
st.area_chart(chart_data)

# bar chart
st.bar_chart(chart_data)

# diagram
st.graphviz_chart("graph object")
```

Code Example:
```python
# importing library.
import streamlit as st
import pandas as pd
import numpy as np


# line chart
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# area chart
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])

st.area_chart(chart_data)

# bar chart
chart_data = pd.DataFrame(
	np.random.randn(50, 3),
	columns=["a", "b", "c"])

st.bar_chart(chart_data)

# flow chart
st.graphviz_chart('''
	digraph {
		start_new_project -> plan_to_learn_new_skills
		plan_to_learn_new_skills -> too_many_skills_to_learn
		too_many_skills_to_learn -> abandon_the_project
		abandon_the_project -> start_another_new_project
		start_another_new_project -> plan_to_learn_new_skills
		plan_to_learn_new_skills -> accidently_learn_all_those_new_skills
		accidently_learn_all_those_new_skills -> complete_the_project
		complete_the_project -> open_source_the_project
		}
	''')
```

<hr>

<a  id="media"></a>
### Media

Streamlit also allows us to add-in media files like images, audios and videos. And the best part about it is that you don't necessarily need to have media file stored in your system you can add the media files via link also.

Syntax:
```sh
# image file.
st.image("file_name or link")

# video file.
st.video("file_name or link")

# bar chart
st.audio(("file_name or link")
```

Code Example:
```python
# importing library.
import streamlit as st

# existing image
st.image("image.jpeg")

# image via link
st.image("https://pbs.twimg.com/profile_images/1366779897423810562/kn7ucNPv_400x400.png")

# exisiting video
st.video("video.mp4") 

# video via link
st.video("https://www.youtube.com/watch?v=EDQeVhG-68Y")

# audio
st.audio("audio.mp3")
```

<hr>

<a  id="Widgets"></a>
### Widgets

So We finally reached this part. Streamlit Widgets are one necessary topic since we can take a lot of inputs from user using these. Following are the some of the important widgets and each widget has it's own functionality depending upon the requirements.

 - **Buttons**: As name says it's a button. Certain operation is performed when a button is pressed or trigger. Button as default will return false and when it is pressed it will return true.
 
	 Syntax:
	```sh
	st.button("button value")
	```
 - **Text Inputs**: Here we can accept text input from user. Basically it will store the input of the user that is entered in the dialog box and you can easily it by assigning a variable to it.
 
	 Syntax:
	```sh
	st.text_input("text label")
	```
 - **Text Area**: Text area is as similar as Text input but here you can take lengthier input such as customer's feedback. The Dialog box will be much bigger than text input and it can be also access via assigning a variable.
 
	 Syntax:
	```sh
	st.text_area("text label")
	```
 - **Check Boxes**:  These are square boxes with message infront of it, usually you see this in terms and conditions agreement where you just blindly select box and hit enter. By default these will be false and also you modify vice versa too.
 
	 Syntax:
	```sh
	# value is default value.
	st.checkbox("message", value=True or False)
	```
 - **Radio Buttons**: Radio buttons are similar as checkbox where user can just select it but here these will be in circle shape and user can choose one in multiple choice. Usually you will see these types in online forms while selecting one from multiple options.

	Syntax:
	```sh
	# index is default value.
	st.radio("label", ["list", "of", "multiple", "optiond"], index=0)
	```

 - **Select boxes**: Select boxes are similar to radio button where user can select one from multiple options and here this will be in drop-down format in which user must click and scroll through the options.

	 Syntax:
	```sh
	# index is default value.
	st.selectbox("label", ["list", "of", "multiple", "optiond"], index=0)
	```

 - **Multi-Select**: Multi select boxes are similar to select boxes but here user can select multiple option at a same time.
 
	 Syntax:
	```sh
	# index is default value.
	st.multiselect("label", ["list", "of", "multiple", "optiond"])
	```
 
 - **Slider**: Slider is fun yet intuitive widget where in user can slide the pointer in linear motion to select the desired value, just like adjusting brightness or music in phones. Here streamlit offers a lot of parameters in it like minimum value, maximum values and step interval values with default value.
 
	 Syntax:
	```sh
	# value is default value with step as interval.
	st.slider("label", min_value=-10, max_value=10, value=0, step=2)
	```

 - **File Uploader**: As name says here we can accept media or file as input. This can accept any file types like image, video, audio and even zip and rar file which make this as powerful and handy widget.
 
	 Syntax:
	```sh
	st.file_uploader("label")
	```
Code Example:
```python
# importing library.
import streamlit as st


# button.
if st.button("Demo Button"):
	st.write("# Hola HUGE TTEEXXTTSSS :joy:.")

# text input.
name = st.text_input("what's your made name?")

if name:
	st.write("Oh, I see! That's your made up name **{0}**".format(name))

# text area.
text_area = st.text_area("How you felt? When you got Spiderman:No way home's spoilers :smirk:")

if text_area:
	st.write(text_area)
	
# check box.
if st.checkbox("Do you agree with this without reading it?"):
	st.write("son of gun, I'm in.!!")

# with default value.
if st.checkbox("Uncheck this one, If you think HTML is not programming language?", value=True):
	st.write("Really Bro.!?")
else:
	st.write("Now We cool")

# radio button
radio = st.radio("Choose one", ["Tobey Maguire", "Andrew Garfield", "Tom Holland", "Dialemma!?"], index=3)

if radio and radio == "Tobey Maguire":
	st.write("The OG Fan ah!")
elif radio and radio == "Andrew Garfield":
	st.write("ngl he is amazing too!")
elif radio and radio == "Tom Holland":
	st.write("This kid got a heart!")
else:
	st.write("Select one bro, quick..!!")

# selectbox
option = st.selectbox(
		'Most popular programming language for 2022?',
		['Python', 'JavaScript', 'GO', 'C++'], index=0)

st.write('You selected:', option)

# multiselect
st.multiselect('select anything', ['a', 'b', 'c'])

# slider
slider = st.slider('sliders', min_value=-10, max_value=10, value=0, step=2)

if  slider > 0:
	st.write("#### %d"%slider)

# file upload.
file_name = st.file_uploader("upload here")

if  file_name:
	if file_name.type == "image/jpeg" or file_name.type == "image/png" or file_name.type == "image/jpg":
		st.image(file_name)

	elif file_name.type == "audio/mpeg":
		st.audio(file_name)

	elif file_name.type == "video/mp4":
		st.video(file_name)

	else:
		st.write(file_name)
```

<hr>

<a  id="sidebars"></a>
### Sidebars

Sidebars are the navbars in streamlit. Since Streamlit doesn't support navbars officially as per now but we can use sidebars to get it done. Sidebar will be appearing hamburger icon in the app where user can click on the icon which will open a sidebar where options are mentioned where clicking on them will perform the selected task. Here you just need to add sidebar in front of widget element and boom you will have that option on sidebar and that's it.!

Syntax:
```sh
st.sidebar.<widget_element>("element value")
```

And now I am being lazy will not explain what all widgets do again, you can refer [widget](#Widgets) for that and I will use previous code for this with sidebar infront of each elements.

```python
# importing library.
import streamlit as st

# sidebar.
side_bar = st.sidebar.button("Demo Button")

if side_bar:
	st.write("# You just clicked the button on side bar.")

name = st.sidebar.text_input("what's your made name?")

if name:
	st.write("# you entered _%s_."%name)

text_area = st.sidebar.text_area("How you felt? When you got Spiderman:No way home's spoilers:smirk:")

if text_area:
	st.write(text_area)

if st.sidebar.checkbox("Do you agree with this without reading it?"):
	st.write("son of gun, I'm in.!!")

if st.sidebar.checkbox("Uncheck this one, If you think HTML is not programming language?", value=True):
	st.write("Really Bro.!?")
else:
	st.write("Now We cool")

radio = st.sidebar.radio("Choose one", ["Tobey Maguire", "Andrew Garfield", "Tom Holland", "Dialemma!?"], index=3)

if radio and radio == "Tobey Maguire":
	st.write("The OG Fan ah!")
elif radio and radio == "Andrew Garfield":
	st.write("ngl he is amazing too!")
elif radio and radio == "Tom Holland":
	st.write("This kid got a heart!")
else:
	st.write("Select one bro, quick..!!")

option = st.sidebar.selectbox(
	'Most popular programming language for 2022?',
	['Python', 'JavaScript', 'GO', 'C++'], index=0)

st.write('You selected:', option)

st.sidebar.multiselect('select anything', ['a', 'b', 'c'])

slider = st.sidebar.slider('sliders', min_value=-10, max_value=10, value=0, step=2)

if slider > 0:
	st.write("#### %d"%slider)

file_name = st.sidebar.file_uploader("upload here")

if file_name:
	if file_name.type == "image/jpeg" or file_name.type == "image/png" or file_name.type == "image/jpg":
		st.image(file_name)
	elif file_name.type == "audio/mpeg":
		st.audio(file_name)
	elif file_name.type == "video/mp4":
		st.video(file_name)
	else:
		st.write(file_name)
```

With sidebars We can do a lot of things and We will see about it in later part of this course.

<hr>

<a  id="animations"></a>
### Animations

You have already seen so many good stuff about streamlit and to elevate this feeling streamlit also going to come with animations too.

Syntax:
```sh
# success message.
st.success() 

# info message.
st.info()

# warning message.
st.warning()

# error message.
st.error()

# exception message is interesting one.
try:
	# some bug in code.
except Exception as e:
	st.exception(e)
```

These are some of basic animations and there some handy and appealing animations like progress bar and time spinner too.

Syntax:
```sh
# progress bar.
progress_bar = st.progress(0)

for i in range(#some range):
	progress_bar.progress(i+1)

# spinner.
with st.spinner("message"):
	#until this block gets completed.

# this one is bonus, which is balloons.
st.balloons()
```

Code Example:
```python
# importing library.
import streamlit as st
import time

# success message.
st.success("Success in Green")

# info message.
st.info("Info in Blue")

# warning message.
st.warning("Warning in Yellow")

# error message.
st.error("Error in Red")

# exception message is interesting one.
try:
	print(some_undefined_variable)
except Exception as e:
	st.exception(e)

# progress bar.
progress_bar = st.progress(0)

for i in range(100):
	time.sleep(0.25)
	progress_bar.progress(i+1)

# this one is really bonus.
st.write("### Balloonssss")
st.balloons()

# spinner.
with st.spinner('spinner for 5 secs..'):
	time.sleep(5)

st.success('### Done!')
st.write("### Again Balloonssss :joy:")
st.balloons()
```

<hr>

:warning: :rotating_light: Are you just scrolling through or writing the code by yourself, If you are just scrolling through this then stop it right now and START CODINNNGG..!!! :rotating_light: :warning: 

<hr>
