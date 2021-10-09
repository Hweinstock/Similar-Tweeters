import React, { Component } from "react";
import Button from '@material-ui/core/Button';

export default class CompareButton extends Component {

  render() {
    return (
        <Button onClick={this.props.onClick}
                variant="contained"
                color="primary"
                size="large">
            compare
        </Button>
    );
  }
}