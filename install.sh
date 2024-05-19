#!/bin/bash

# Directorios
dotfiles_dir="/home/$USER/DotFiles"  # Directorio principal de los dotfiles
themes_dir="$dotfiles_dir/themes"  # Directorio que contiene los temas Material y Nightfox
material_dir="$themes_dir/material"  # Directorio del tema Material
nightfox_dir="$themes_dir/nightfox"  # Directorio del tema Nightfox
config_dir="/home/$USER/.config"  # Directorio de configuración en /home del usuario actual
backup_dir="$config_dir/backup"  # Directorio de respaldo dentro de .config

# Función para mostrar el menú de opciones
show_menu() {
    echo "Seleccione una opción:"
    echo "1. Material Theme"
    echo "2. Nightfox Theme"
    echo "3. Salir"
}

# Función para copiar los archivos de configuración con barra de progreso
copy_config_files() {
    local theme_dir="$1"  # Directorio del tema seleccionado
    local config_files=("qtile" "dunst" "alacritty" "rofi")  # Lista de directorios de configuración a copiar

    # Verificar si existen los directorios en .config
    if [ -d "$config_dir/qtile" ] && [ -d "$config_dir/dunst" ] && [ -d "$config_dir/alacritty" ] && [ -d "$config_dir/rofi" ]; then
        echo "Los directorios de configuración ya existen en $config_dir."
        echo "Se creará un respaldo en: $backup_dir"
        if [ ! -d "$backup_dir" ]; then
            mkdir -p "$backup_dir"
            mv "$config_dir/qtile" "$config_dir/dunst" "$config_dir/alacritty" "$config_dir/rofi" "$backup_dir"
            sleep 3  # Retardo de 3 segundos
        fi
    else
        echo "No se encontraron directorios de configuración en $config_dir."
        sleep 3  # Retardo de 3 segundos
    fi

    # Copiar archivos de configuración del tema seleccionado con barra de progreso
    for config_file in "${config_files[@]}"; do
        if [ -d "$theme_dir/$config_file" ]; then
            echo "Copiando $config_file..."
            cp -r "$theme_dir/$config_file" "$config_dir" | pv -lep -s $(du -sb "$theme_dir/$config_file" | awk '{print $1}') > /dev/null
            echo "Copiado con éxito: $config_file"
            sleep 3  # Retardo de 3 segundos
        fi
    done
}

# Bucle principal
while true; do
    show_menu
    read -p "Ingrese su opción: " option

    case $option in
        1)
            copy_config_files "$material_dir"
            sleep 3  # Retardo de 3 segundos
            ;;
        2)
            copy_config_files "$nightfox_dir"
            sleep 3  # Retardo de 3 segundos
            ;;
        3)
            echo "Saliendo del script..."
            exit 0
            ;;
        *)
            echo "Opción inválida. Intente nuevamente."
            sleep 3  # Retardo de 3 segundos
            ;;
    esac
done
