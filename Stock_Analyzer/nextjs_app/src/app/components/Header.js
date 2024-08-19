import React from 'react';

const Header = () => {
    return (
        <header style={styles.header}>
            <h1 style={styles.title}>Stock Guru AI</h1>
            <p style={styles.subtitle}>Your Ultimate Companion for Stock Analysis and Investment</p>
        </header>
    );
};

const styles = {
    header: {
        textAlign: 'center',
        padding: '50px 20px',  // Adjusted padding for a balanced look
        backgroundColor: '#145da0',  // Reverted to the previous dark blue background
        boxShadow: '0 6px 15px rgba(0, 0, 0, 0.15)',  // Slightly deeper shadow
        borderBottom: '5px solid #ffdd00',  // Adds a yellow underline for emphasis
    },
    title: {
        fontSize: '3.5rem',  // Larger font size for a more impactful title
        fontWeight: '900',
        color: '#ffffff',  // White text color
        letterSpacing: '3px',  // Enhanced letter spacing for clarity
        textTransform: 'uppercase',
        margin: '0',  // Remove default margin
    },
    subtitle: {
        fontSize: '1.2rem',  // Add a subtitle for a professional touch
        color: '#ffdd00',  // Match the border color for consistency
        letterSpacing: '1px',
        marginTop: '10px',
    }
};

export default Header;