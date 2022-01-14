
## Hey There..! I am **[Sudeep Nellur](sudeepnellur.tech)** aka **[Jairus313](sudeepnellur.tech)** :sunglasses:. Here I am writing this little crash course about **[Streamlit.io](streamlit.io)** which will be more than enough for you to get started and start rolling some cool apps. So let's wrap our head around.!

  
### About Streamlit..!

Before starting with actually let's answers some basics questions.

Q. What is the Streamlit.io?</br>
A. Streamlit.io is the app framework for machine learning and data science solution where you can write few lines of python code and get your app up running within minutes and you can host too, if you want to share with your friends. More on [Streamlit.io](streamlit.io)</br></br>

Q. Why Streamlit.io or UI in general needed?</br>
A. <img  src="tweet.png"  alt="https://twitter.com/jairus313/status/1472974950508089348?s=20"  width="500"/>

Q. What are the pre-requisites?</br>
A. Streamlit is python framework, So Python is must and enough but if you already know Python GUI like PyQt or TKinter and HTML then it would be really.

With these being clear to you, let's start and feel free to jump around on the topic with which you are interested.

### Index

- [Installation and Get started](#Installation)
- [General Synatx](#general_syntax)
- [Markdowns](#markdown)
- [Latex](#latex)
- [Write](#write)
- [Display](#display)
- [Plots](#plot)
- [Media](#media)

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
	import  streamlit  as  st

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
	import  streamlit  as  st

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
	import  streamlit  as  st
	import  pandas  as  pd
	import  numpy  as  np

	# to print anything using write.
	st.write(1234)

	st.write("# Can be used as markdown too.")

	st.write("sum of two values", 2+2)

	  

	# can display the arrays too.
	data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
	columns=['a', 'b', 'c'])

	st.write("before the dataframe", data, "after the dataframe")
```

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
	import  streamlit  as  st
	import  pandas  as  pd
	import  numpy  as  np

	# dataframe.
	# values in 2D array with column name.
	df = pd.DataFrame(
	np.array([["Sudeep Nellur", "Machine Learning Engineer", "https://sudeepnellur.tech/"]]),
	columns=("Name", "Desgination", "Portfolio"))
	
	st.dataframe(df)

	df = pd.DataFrame(
	np.random.randn(10, 10),
	columns=('col %d' % i  for  i  in  range(10)))

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
	import  streamlit  as  st
	import  pandas  as  pd
	import  numpy  as  np

	  
	  

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
	import  streamlit  as  st

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