import React, { Component } from "react";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import statBoxStyle from './shared_styling/statBox.module.css';

export default class StatBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            headers: []
        };

    }


    componentDidMount() {
        this.props.get_headers()
            .then(result => this.setState({headers: result.data.Headers}))
            .catch(error => console.log(error));
    }

    generate_rows() {
        let rows;

        if (typeof this.props.data.rows == 'undefined') {
            rows = [];
        } else {
            rows = new Array(this.props.data.rows.length);
            this.props.data.rows.forEach(function (item, index) {
                rows[index] = item;
                rows[index].name = item.author
        });
        }
        return rows;
    }

    format_data() {
        if (typeof this.props.data != 'undefined') {
            let rows = this.generate_rows(this.props.data);

            return (
                <TableBody>
                {rows.map(row => (
                    <TableRow key={row.name}>
                        <TableCell component="th" scope="row">
                            {row.name}
                        </TableCell>
                        {this.state.headers.map(header => (
                            <TableCell key={[header]} style={{textAlign: "right"}}>
                                {row.[header]}
                            </TableCell>
                            )
                        )}
                    </TableRow>

                ))}
            </TableBody>);

        } else {

            return ( <TableBody></TableBody> );
        }
    }

    format_headers() {

        return (
            <TableRow>
                <TableCell key={"blank"}> {' '} </TableCell>
                {this.state.headers.map(header =>
                    <TableCell style={{textAlign: "right"}} key={header}>{header}</TableCell>)}
            </TableRow>
        )


    }

    render() {
        return (
            <div className={statBoxStyle.default}>
            <TableContainer component={Paper}>
                <Table size="small" aria-label="a dense table">
                    <TableHead>
                        {this.format_headers()}
                    </TableHead>
                    {this.format_data()}
                </Table>
            </TableContainer>
            </div>
        );
  }
}