# IAS - Trabajo Practico

Este proyecto corresponde al TP de la materia Implementacion y Actualizacion de Software (Universidad de Moron, 2026).

## Objetivo

Diseñar, implementar y demostrar un pipeline completo de CI/CD, incluyendo:

- Pull Request
- Herramientas de testing
- QA
- Despliegue a produccion con aprobacion manual

Conceptos a desarrollar:

- CI/CD real
- Trabajo en equipo distribuido
- Control de calidad
- Despliegue controlado
- Autorizaciones

## Contexto

La empresa IAS desarrolla APIs para clientes y ya tiene definida una solucion corporativa de CI/CD.
Cada alumno simula ser empleado de IAS y desarrolla una API para un cliente ficticio, respetando proceso y herramientas corporativas en entorno local y remoto.

## Requisitos

### Local

- PC local
- Internet
- Python 3.x
- Git
- Visual Studio Code

### Remoto (GitHub)

- Cuenta en GitHub
- Repositorio: ias_apellido_api
- Secrets (Secrets and variables):
	- RENDER_DEPLOY_HOOK_DEV
	- RENDER_DEPLOY_HOOK_QA
	- RENDER_DEPLOY_HOOK_PRD
- Environment:
	- production con Required reviewers = TRUE

### Remoto (Render)

- Cuenta en Render
- 3 Web Services: DEV, QA y PRD
- Configuracion sugerida:
	- name: apellido_api-* (dev, qa o prd)
	- Repository: https://github.com/nombre_organizacion/ias_apellido_api
	- Build Command:
		- DEV y QA: pip install -r requirements-dev.txt
		- PRD: pip install -r requirements.txt
	- Auto-Deploy: OFF
- Base de datos Postgres:
	- Se crea 1 base (plan gratuito)
	- Puede ser compartida entre DEV/QA/PRD solo para fines educativos

## Alcance Tecnico

La API puede ser basica (ejemplo: ABM de usuarios).

Minimos obligatorios:

- Flask
- Pytest
- Bandit
- Al menos 3 endpoints (incluyendo healthcheck)
- Respuestas en JSON
- Frontend opcional

## Consideraciones de Servicio

- En Render (plan basico), el primer request puede tardar varios minutos.
- Si el servicio queda inactivo, puede apagarse y volver a demorar al iniciar.
- La base de datos expira al mes: contemplar recupero rapido.

## Arquitectura Sugerida

Repositorio GitHub:

- app (API Flask)
- tests/
	- unit/
	- integration/
	- security/
- requirements.txt
- requirements-dev.txt
- workflows (CI/CD)

## Flujo CI/CD Obligatorio (Estandar IAS)

1. Developer hace push a feature branch.
2. Pull Request de feature a develop.
3. Corre CI pipeline.
4. Code Review y Approval.
5. Merge y deploy a DEV.
6. Pull Request de develop a main.
7. Corre CI pipeline.
8. Code Review y Approval.
9. Merge y deploy a QA.
10. Aprobacion manual a PRD.
11. Deploy a PRD.

## Requisitos Tecnicos Obligatorios

### CI (GitHub Actions, al crear PR)

Debe incluir:

- Tests unitarios
- Tests de integracion
- Analisis con Bandit
- Tests de seguridad (solo en PR de develop a main)

### CD (GitHub Actions)

- Deploy automatico a DEV (develop)
- Deploy automatico a QA (main)
- Deploy manual a PRD (aprobacion)

### Seguridad y configuracion

- Usar variables de entorno (ENV, DEBUG)
- No hardcodear debug=True
- Bandit sin errores criticos

## Rol del Release Manager

El deploy a produccion no es automatico y requiere aprobacion manual.

El release manager (el mismo alumno) solo aprueba si:

- QA funciona correctamente
- No hay errores criticos
- El sistema esta estable

## Entregables

Cada alumno debe entregar:

- Repositorio GitHub con:
	- Codigo de la API
	- Workflows CI/CD
	- Estructura correcta
- Evidencias en vivo el dia de entrega:
	- PR creado
	- CI ejecutandose
	- Deploy en DEV
	- Deploy en QA
	- Aprobacion manual
	- Deploy en PRD

## Evaluacion

### Tecnica (60%)

- CI funciona correctamente
- CD funciona correctamente
- Uso correcto de entornos
- Bandit sin errores criticos

### Proceso (30%)

- Uso correcto de PR
- Uso correcto de ramas
- Respeto del flujo Empresa IAS

### Presentacion (10%)

- Claridad

## Datos de Catedra

- Universidad de Moron
- Docente: Marcelo Camicha
- Año: 2026
