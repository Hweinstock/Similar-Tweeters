import ProgressBar from 'react-bootstrap/ProgressBar'
import React, { Component } from "react";

import textBoxStyle from "./styling/textBox.module.css"

export default class GuessBar extends Component {

    constructor(props) {
        super(props);

    }

    determine_color(percent) {
        if(percent > 2/3*100){
            // Green Bar for more than 2/3
            return "success"
        }

        if(percent < 1/3*100){
            // Red Bar for less than 1/3
            return "danger"
        }
        // Yellow bar for less than 2/3 but greater than 1/3
        return "warning"

    }

    render() {
        return (

            <div className={textBoxStyle.guessBar}>
            <h2> Similarity </h2>
            <ProgressBar
                variant={this.determine_color(this.props.percent)}
                now={this.props.percent}
                label={this.props.percent+'%'}
                style={{color: 'black'}}
            />
            </div>
        );
    }
}