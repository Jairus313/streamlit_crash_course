## Hey There..! I am **[Sudeep Nellur](sudeepnellur.tech)** aka **[Jairus313](sudeepnellur.tech)** :sunglasses:. Here I am writing this little crash course about **[Streamlit.io](streamlit.io)** which will be more than enough for you to get started and start rolling some cool apps. So let's wrap our head around.!

### About Streamlit..!

Before starting with actually let's answers some basics questions.

Q. What is the Streamlit.io?</br>
A. Streamlit.io is the app framework for machine learning and data science solution where you can write few lines of python code and get your app up running within minutes and you can host too, if you want to share with your friends. More on [Streamlit.io](streamlit.io)</br></br>

Q. Why Streamlit.io or UI in general needed?</br>
A. ![tweet](tweet.png)</br></br>

Q. What are the pre-requisites?</br>
A. Streamlit is python framework, So Python is must and enough but if you already know Python GUI like PyQt or TKinter then it would be  really.

With these being clear to you, let's start and feel free to jump around on the topic with which you are interested.

### Index

 - [Installation and Get started](#Installation)
 - 


<a id="Installation"></a>
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

**Note:**  Streamlit in background uses protobuf as it's internal dependencies, Install Google protobuf before installing streamlit first. For more refer this [link](https://stackoverflow.com/questions/61922334/how-to-solve-attributeerror-module-google-protobuf-descriptor-has-no-attribu) .

Now that you have installed it properly, Create python script and write the below code.

```python
	# importing library, will be using it as "st" throughtout the blog.
	import  streamlit  as  st

	# Just a title, will get on this later.
	st.title('Just a title')
```

Save this script then open the terminal and run below the command which will make app to boot up and this will open your browser for it.

```sh
	streamlit run your_script_name.py
```
