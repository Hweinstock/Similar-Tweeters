import ProgressBar from 'react-bootstrap/ProgressBar'
import React, { Component } from "react";

export default class GuessBar extends Component {

    constructor(props) {
        super(props);

    }

    render() {
        return (
            <div style={{width: '20%'}}>
                <h2> Similarity: </h2>
            <ProgressBar
                variant="success"
                now={this.props.percent}
                label={this.props.percent+'%'}
            />
            </div>
        );
    }
}