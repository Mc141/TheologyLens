import ThemeTag from "./ThemeTag";

function ThemesHeader() {
    return <div>
        <h2 className="theme-title">Themes</h2>
        <div id="themes-container">
            
            <ThemeTag></ThemeTag>

            <ThemeTag></ThemeTag>
            
            <ThemeTag></ThemeTag>
        </div>
    </div>
}



export default ThemesHeader;