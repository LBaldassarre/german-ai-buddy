import './App.css'
import SidePane from './components/SidePane/SidePane'
import Chat from './pages/Chat'

function App() {

  return (
    <>
      <div className="app-container">
        <SidePane/>
        <Chat/>
      </div>
    </>
  )
}

export default App
