import React, { Component } from "react";
import './nav.css';
import logo from '../img/petBookLogo_white.png'

class Nav extends Component {

    displayRegister() {
        this.props.setAuthState({
            register: true,
            showUserForm: true
        })
    }

    displayLogin() {
        this.props.setAuthState({
            register: false,
            showUserForm: true
        })
    }

    //   displayProdForm() {
    //     this.props.displaySell()
    //   }

    logOut() {
        this.props.logOut()
    }

    render() {
        const isAuth = this.props.isAuth
        console.log("isAuth?", isAuth)
        return (
            <nav>
                <div class="brand">
                    <img id="home" src={logo} alt="logo" />
                    <h3>PetBook</h3>
                </div>
                {isAuth &&
                    <div class="nav__links">
                        <button>Add Pet</button>
                        <button>Follow</button>
                        <h3>Welcome, {this.props.user}</h3>
                    </div>
                }
                <div>
                    <button onClick={() => isAuth ? this.logOut() : this.displayLogin()}>
                        Log {isAuth ? "out" : "in"} </button>
                    <button onClick={() => this.displayRegister()}>Register</button>
                </div>
            </nav >
        )
    }
}

export default Nav