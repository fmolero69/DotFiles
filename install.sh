#!/bin/bash


# Directorios
dotfiles_dir="$HOME/DotFiles"
themes_dir="$dotfiles_dir/themes"
material_dir="$themes_dir/material"
nightfox_dir="$themes_dir/nightfox"
config_dir="$HOME/.config"
backup_dir="$config_dir/backup"

# Función para mostrar el menú de opciones
show_menu() {
    echo "Seleccione una opción:"
    echo "1. Material Theme"
    echo "2. Nightfox Theme"
    echo "3. Salir"
}

# Función para copiar los archivos de configuración
copy_config_files() {
    local theme_dir="$1"
    local config_files=("qtile" "dunst" "alacritty" "rofi")

    # Verificar si existen los directorios en .config
    if [ -d "$config_dir/qtile" ] && [ -d "$config_dir/dunst" ] && [ -d "$config_dir/alacritty" ] && [ -d "$config_dir/rofi" ]; then
        if [ ! -d "$backup_dir" ]; then
            mkdir -p "$backup_dir"
            mv "$config_dir/qtile" "$config_dir/dunst" "$config_dir/alacritty" "$config_dir/rofi" "$backup_dir"
        fi
    fi

    # Copiar archivos de configuración del tema seleccionado
    cp -r "$theme_dir/qtile" "$theme_dir/dunst" "$theme_dir/alacritty" "$theme_dir/rofi" "$config_dir"
}

# Bucle principal
while true; do
    show_menu
    read -p "Ingrese su opción: " option

    case $option in
        1)
            copy_config_files "$material_dir"
            ;;
        2)
            copy_config_files "$nightfox_dir"
            ;;
        3)
            echo "Saliendo del script..."
            exit 0
            ;;
        *)
            echo "Opción inválida. Intente nuevamente."
            ;;
    esac
done
