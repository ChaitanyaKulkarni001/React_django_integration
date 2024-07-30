import React ,{Componant}from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'


export default class Main extends   Componant{

  render(){
    return(
      <Main>
        <App />
      </Main>
    )
  }
}

const appDiv = document.getElementById('app');
render (<Main/>,appDiv)

// ReactDOM.createRoot(document.getElementById('root')).render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
// )
