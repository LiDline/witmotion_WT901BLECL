import React from "react";
import "./App.css";
import Grid from "@mui/material/Grid"; // Grid version 1
import { ButtonSearch } from "./Buttons";
import { BasicSelect } from "./Select";

export function App() {
  return (
    <Grid container spacing={2}>
      <Grid item xs={12}>
        <h1 className="App-Header">WT901BLE</h1>
      </Grid>
      <Grid item xs={12}>
        <div className="App-Hor-Line"></div>
      </Grid>
      <div className="App-Pages">
        <Grid item xs={12}>
          <ButtonSearch />
        </Grid>
      </div>
    </Grid>
  );
}
