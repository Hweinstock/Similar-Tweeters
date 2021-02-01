import React, { Component } from "react";
import Button from '@material-ui/core/Button';

export default class SubmitButton extends Component {

  render() {
    return (
        <Button variant="contained"
                color="primary"
                onClick={this.props.onClick}>
            submit
        </Button>
    );
  }
}