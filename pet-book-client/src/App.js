import React, { Component } from 'react';
import Auth from './auth'
import Nav from './nav'
import './App.css';
import DashBoard from './dashboard/board';
import Profile from './profile/profile';


class App extends Component {

  state = {
    username: "",
    password: "",
    first_name: "",
    last_name: "",
    email: "",
    street: "",
    city: "",
    state: "",
    zip: "",
    isAuth: false,
    register: false,
    showUserForm: false,
    user: "",
    showSellForm: false,
    userPets: [],
    followedPets: [],
    currentView: 'home',
    profileData: []
  }

  
  
  
  setAuthState(authObj) {
    this.setState(authObj)
  }
  
  logOut() {
    console.log("log OUT", localStorage.getItem("token"));
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    localStorage.removeItem("id");
    // Set everything to false again?
    this.setAuthState({
      isAuth: false,
      user: "",
    })
    console.log(localStorage.getItem("token"));
  }
  
  getuserPets() {
    let token = localStorage.getItem("token")
    fetch(`http://127.0.0.1:8000/user-pets/`, {
      method: 'GET',
      headers: {
        "Authorization": `Token ${token}`
      }
    })
    .then((response) => {
      return response.json();
    })
    .then((pets) => {
      console.log('userPets', pets);
      this.setState({ userPets: pets })
    })
    .catch((err) => {
      console.log("fetch no like you, brah", err);
    })
  }
  
  getFollowedPets() {
    let token = localStorage.getItem("token")
    fetch(`http://127.0.0.1:8000/followed-pets/`, {
      method: 'GET',
      headers: {
        "Authorization": `Token ${token}`
      }
    })
    .then((response) => {
      return response.json();
    })
    .then((owner) => {
      const follows = owner[0].follows
      this.setState({ followedPets: follows })
    })
    .catch((err) => {
      console.log("fetch no like you, brah", err);
    })
  }
  
  ProfileHandler = function(url) {
    let token = localStorage.getItem("token")
    fetch(`${url}`, {
      method: 'GET',
      headers: {
        "Authorization": `Token ${token}`
      }
    })
    .then((response) => {
      return response.json();
    })
    .then((pet) => {
        const petData = []
        petData.push(pet)
        console.log("petdata", petData)
        // debugger
        this.setState({ 
          profileData: petData
        })
      })
      .catch((err) => {
        console.log("fetch no like you, brah", err);
      })
    }.bind(this)

    
componentDidMount() {
      let token = localStorage.getItem("token")
      let user = localStorage.getItem("user")
      if (token) {
        console.log("User still logged in", user)
        this.setState({
          isAuth: true,
          user: user
        });
      }
      this.getuserPets()
      this.getFollowedPets()
      // this.ProfileHandler()
  
      // }
    }
  

  showView = function (e, data) {
    let view = null

    // Click event triggered switching view
    if (e.hasOwnProperty("target")) {
      view = e.target.id.split("__")[1]

      // View switch manually triggered by passing in string
    } else {
      view = e
      console.log("view changed brah!")
    }
    // if (view === "profile") {
    //   this.setState({ currentView: "profile"})

    // }
    // Update state to correct view will be rendered
    this.setState({
      currentView: view,
    })

  }.bind(this)

  View = () => {
    if (this.state.isAuth === false) {
      return this.state.showUserForm ? <Auth authState={this.state} setAuthState={(obj) => this.setAuthState(obj)} /> : null
    }
    else if (this.state.isAuth === true) {
      switch (this.state.currentView) {
        case 'home':
          return <DashBoard userPets={this.state.userPets} followedPets={this.state.followedPets} viewHandler={this.showView} ProfileHandler={(url)=>{this.ProfileHandler(url)}}/>
        case 'profile':
          return <Profile resource={this.state.profileData}/>
        default:
          return <DashBoard userPets={this.state.userPets} followedPets={this.state.followedPets} viewHandler={this.showView} ProfileHandler={(url)=>{this.ProfileHandler(url)}}/>  

      }
    }
  }
  
  render() {
    return (
      <div className="App">
        <Nav isAuth={this.state.isAuth} user={this.state.user} setAuthState={(obj) => this.setAuthState(obj)} displaySell={() => this.displaySell()} logOut={() => this.logOut()} viewHandler={this.showView}/>
          {this.View()}
      </div>
    );
  }
}

export default App;
