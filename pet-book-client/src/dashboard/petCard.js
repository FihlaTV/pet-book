import React, { Component } from "react";

import { Box, Button } from 'bloomer';
import 'bulma/css/bulma.css';
import avatar from "../img/petBookLogo_white.png"
import "./dashboard.css"


class CustomCard extends Component {
    uniqueKey = 1

    render() {
        return (
            <div className="container_dashboard"> 
            {this.props.resource.map(c => (
                <div key={this.uniqueKey+=1}>
                <Box className="card_pet"> 
                    {c.image === "" ? <img src={c.image} alt={c.name} /> : <img src={avatar} alt="default avatar"/>}
                    <Button isSize={4} id="pet__profile" 
                    onClick={()=>{
                        this.props.ProfileHandler(c.url)
                        this.props.viewHandler('profile')
                    }}>{c.name}</Button>
                </Box>
                </div>
                ))}
            </div>
        )
    }
}

export default CustomCard
